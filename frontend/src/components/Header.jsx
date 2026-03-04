import React from 'react';
import { Waves } from 'lucide-react';

const Header = () => {
  return (
    <header className="bg-white shadow-sm border-b">
      <div className="max-w-7xl mx-auto px-4 py-4">
        <div className="flex items-center gap-3">
          <div className="bg-green-600 p-2 rounded-lg">
            <Waves className="w-6 h-6 text-white" />
          </div>
          <div>
            <h1 className="text-2xl font-bold text-gray-900">
              EcoSound Monitor
            </h1>
            <p className="text-sm text-gray-600">
              Automated Wildlife Compliance for Renewable Energy
            </p>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
