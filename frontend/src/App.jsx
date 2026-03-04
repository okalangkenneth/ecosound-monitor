import React, { useState, useEffect } from 'react';
import { Upload, FileAudio, BarChart3, FileText } from 'lucide-react';
import axios from 'axios';
import FileUpload from './components/FileUpload';
import Dashboard from './components/Dashboard';
import Header from './components/Header';

const API_URL = 'http://localhost:8000/api';

function App() {
  const [stats, setStats] = useState(null);
  const [recordings, setRecordings] = useState([]);
  const [selectedRecording, setSelectedRecording] = useState(null);
  const [detections, setDetections] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchStats();
    fetchRecordings();
  }, []);

  const fetchStats = async () => {
    try {
      const response = await axios.get(`${API_URL}/audio/stats`);
      setStats(response.data);
    } catch (error) {
      console.error('Error fetching stats:', error);
    }
  };

  const fetchRecordings = async () => {
    try {
      const response = await axios.get(`${API_URL}/audio/recordings`);
      setRecordings(response.data);
    } catch (error) {
      console.error('Error fetching recordings:', error);
    }
  };

  const fetchDetections = async (recordingId) => {
    try {
      setLoading(true);
      const response = await axios.get(`${API_URL}/audio/recordings/${recordingId}`);
      setDetections(response.data.detections || []);
      setSelectedRecording(recordingId);
    } catch (error) {
      console.error('Error fetching detections:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleUploadComplete = () => {
    fetchStats();
    fetchRecordings();
  };

  const generateReport = async (recordingId) => {
    try {
      const response = await axios.get(
        `${API_URL}/reports/generate/${recordingId}`,
        { responseType: 'blob' }
      );
      
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `compliance_report_${recordingId}.pdf`);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      console.error('Error generating report:', error);
      alert('Error generating report');
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      
      <main className="max-w-7xl mx-auto px-4 py-8">
        <FileUpload onUploadComplete={handleUploadComplete} />
        
        <Dashboard
          stats={stats}
          recordings={recordings}
          detections={detections}
          selectedRecording={selectedRecording}
          loading={loading}
          onSelectRecording={fetchDetections}
          onGenerateReport={generateReport}
        />
      </main>
    </div>
  );
}

export default App;
