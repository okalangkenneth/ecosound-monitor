import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';
import { FileText, Download } from 'lucide-react';

const COLORS = ['#16a34a', '#3b82f6', '#f59e0b', '#ef4444'];

const Dashboard = ({ stats, recordings, detections, selectedRecording, loading, onSelectRecording, onGenerateReport }) => {
  
  const getSpeciesData = () => {
    const speciesCount = {};
    detections.forEach(det => {
      const name = det.common_name;
      speciesCount[name] = (speciesCount[name] || 0) + 1;
    });
    
    return Object.entries(speciesCount)
      .map(([name, value]) => ({ name, value }))
      .sort((a, b) => b.value - a.value)
      .slice(0, 10);
  };

  const getTypeData = () => {
    const birdCount = detections.filter(d => d.detection_type === 'bird').length;
    const batCount = detections.filter(d => d.detection_type === 'bat').length;
    
    return [
      { name: 'Birds', value: birdCount },
      { name: 'Bats', value: batCount }
    ];
  };

  return (
    <div className="space-y-6">
      {/* Stats Cards */}
      {stats && (
        <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
          <StatsCard title="Total Recordings" value={stats.total_recordings} color="blue" />
          <StatsCard title="Total Detections" value={stats.total_detections} color="green" />
          <StatsCard title="Bird Detections" value={stats.bird_detections} color="yellow" />
          <StatsCard title="Bat Detections" value={stats.bat_detections} color="purple" />
          <StatsCard title="Unique Species" value={stats.unique_species} color="red" />
        </div>
      )}

      {/* Recordings List */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-bold mb-4">Recordings</h2>
        
        {recordings.length === 0 ? (
          <p className="text-gray-500">No recordings yet. Upload an audio file to get started.</p>
        ) : (
          <div className="space-y-2">
            {recordings.map(recording => (
              <div
                key={recording.id}
                className={`p-4 border rounded-lg cursor-pointer transition-colors
                  ${selectedRecording === recording.id ? 'border-green-500 bg-green-50' : 'border-gray-200 hover:border-green-300'}`}
                onClick={() => onSelectRecording(recording.id)}
              >
                <div className="flex justify-between items-center">
                  <div>
                    <p className="font-medium">{recording.filename}</p>
                    <p className="text-sm text-gray-500">
                      {new Date(recording.created_at).toLocaleString()} • 
                      {recording.duration.toFixed(1)}s
                    </p>
                  </div>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      onGenerateReport(recording.id);
                    }}
                    className="flex items-center gap-2 px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700"
                  >
                    <Download className="w-4 h-4" />
                    Report
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Detections */}
      {selectedRecording && (
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-xl font-bold mb-4">Detections Analysis</h2>
          
          {loading ? (
            <div className="flex justify-center py-12">
              <div className="animate-spin w-8 h-8 border-4 border-green-600 border-t-transparent rounded-full" />
            </div>
          ) : detections.length === 0 ? (
            <p className="text-gray-500">No detections found.</p>
          ) : (
            <>
              {/* Charts */}
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
                <div>
                  <h3 className="font-semibold mb-3">Top Species Detected</h3>
                  <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={getSpeciesData()}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="name" angle={-45} textAnchor="end" height={100} />
                      <YAxis />
                      <Tooltip />
                      <Bar dataKey="value" fill="#16a34a" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>

                <div>
                  <h3 className="font-semibold mb-3">Detection Type Distribution</h3>
                  <ResponsiveContainer width="100%" height={300}>
                    <PieChart>
                      <Pie
                        data={getTypeData()}
                        cx="50%"
                        cy="50%"
                        labelLine={false}
                        label={({ name, value }) => `${name}: ${value}`}
                        outerRadius={100}
                        fill="#8884d8"
                        dataKey="value"
                      >
                        {getTypeData().map((entry, index) => (
                          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                        ))}
                      </Pie>
                      <Tooltip />
                    </PieChart>
                  </ResponsiveContainer>
                </div>
              </div>

              {/* Detections Table */}
              <div className="overflow-x-auto">
                <h3 className="font-semibold mb-3">All Detections</h3>
                <table className="min-w-full divide-y divide-gray-200">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Species</th>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Common Name</th>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Type</th>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Confidence</th>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Time (s)</th>
                    </tr>
                  </thead>
                  <tbody className="bg-white divide-y divide-gray-200">
                    {detections.map((detection, idx) => (
                      <tr key={idx} className="hover:bg-gray-50">
                        <td className="px-4 py-3 text-sm text-gray-900">{detection.species_name}</td>
                        <td className="px-4 py-3 text-sm text-gray-900">{detection.common_name}</td>
                        <td className="px-4 py-3 text-sm">
                          <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full
                            ${detection.detection_type === 'bird' ? 'bg-yellow-100 text-yellow-800' : 'bg-purple-100 text-purple-800'}`}>
                            {detection.detection_type}
                          </span>
                        </td>
                        <td className="px-4 py-3 text-sm text-gray-900">
                          {(detection.confidence * 100).toFixed(1)}%
                        </td>
                        <td className="px-4 py-3 text-sm text-gray-900">
                          {detection.start_time.toFixed(2)}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
};

const StatsCard = ({ title, value, color }) => {
  const colorClasses = {
    blue: 'bg-blue-50 text-blue-600',
    green: 'bg-green-50 text-green-600',
    yellow: 'bg-yellow-50 text-yellow-600',
    purple: 'bg-purple-50 text-purple-600',
    red: 'bg-red-50 text-red-600',
  };

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <p className="text-sm text-gray-600 mb-1">{title}</p>
      <p className={`text-3xl font-bold ${colorClasses[color]}`}>{value}</p>
    </div>
  );
};

export default Dashboard;
