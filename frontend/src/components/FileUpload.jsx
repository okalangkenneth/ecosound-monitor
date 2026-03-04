import React, { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, FileAudio, CheckCircle, XCircle } from 'lucide-react';
import axios from 'axios';

const FileUpload = ({ onUploadComplete }) => {
  const [uploading, setUploading] = useState(false);
  const [uploadStatus, setUploadStatus] = useState(null);

  const onDrop = useCallback(async (acceptedFiles) => {
    const file = acceptedFiles[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);
    formData.append('location', 'Demo Wind Farm, Sweden');

    setUploading(true);
    setUploadStatus(null);

    try {
      const response = await axios.post(
        'http://localhost:8000/api/audio/upload',
        formData,
        {
          headers: { 'Content-Type': 'multipart/form-data' }
        }
      );

      setUploadStatus({
        success: true,
        message: `Processing complete! Found ${response.data.detections} detections from ${file.name}`
      });

      if (onUploadComplete) {
        onUploadComplete();
      }
    } catch (error) {
      setUploadStatus({
        success: false,
        message: 'Upload failed: ' + (error.response?.data?.detail || error.message)
      });
    } finally {
      setUploading(false);
    }
  }, [onUploadComplete]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'audio/*': ['.wav', '.mp3', '.flac', '.ogg']
    },
    maxFiles: 1
  });

  return (
    <div className="mb-8">
      <div
        {...getRootProps()}
        className={`border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition-colors
          ${isDragActive ? 'border-green-500 bg-green-50' : 'border-gray-300 hover:border-green-400'}
          ${uploading ? 'opacity-50 cursor-not-allowed' : ''}`}
      >
        <input {...getInputProps()} disabled={uploading} />
        
        <div className="flex flex-col items-center gap-4">
          <div className="bg-green-100 p-4 rounded-full">
            {uploading ? (
              <div className="animate-spin w-8 h-8 border-4 border-green-600 border-t-transparent rounded-full" />
            ) : (
              <FileAudio className="w-8 h-8 text-green-600" />
            )}
          </div>
          
          <div>
            <p className="text-lg font-semibold text-gray-700">
              {uploading ? 'Processing audio...' : 
               isDragActive ? 'Drop the audio file here' : 
               'Upload Audio Recording'}
            </p>
            <p className="text-sm text-gray-500 mt-1">
              Drag & drop or click to select WAV, MP3, FLAC, or OGG files
            </p>
          </div>
        </div>
      </div>

      {uploadStatus && (
        <div className={`mt-4 p-4 rounded-lg flex items-start gap-3
          ${uploadStatus.success ? 'bg-green-50 border border-green-200' : 'bg-red-50 border border-red-200'}`}>
          {uploadStatus.success ? (
            <CheckCircle className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
          ) : (
            <XCircle className="w-5 h-5 text-red-600 flex-shrink-0 mt-0.5" />
          )}
          <p className={`text-sm ${uploadStatus.success ? 'text-green-800' : 'text-red-800'}`}>
            {uploadStatus.message}
          </p>
        </div>
      )}
    </div>
  );
};

export default FileUpload;
