@echo off
echo ========================================
echo EcoSound Monitor - Installation Script
echo ========================================
echo.

echo [1/2] Installing Backend Dependencies...
cd backend
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install backend dependencies
    pause
    exit /b 1
)
cd ..

echo.
echo [2/2] Installing Frontend Dependencies...
cd frontend
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install frontend dependencies
    pause
    exit /b 1
)
cd ..

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo To start the application, run: start.bat
echo.
echo Or manually:
echo   Backend:  cd backend  && python main.py
echo   Frontend: cd frontend && npm run dev
echo.
pause
