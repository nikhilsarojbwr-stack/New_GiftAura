@echo off
title GiftAura+ - Simple Auto Push

cd /d D:\gap

echo.
echo ==========================================
echo     GiftAura+ Auto Push
echo ==========================================
echo.

REM ==========================================
REM 1. Pull latest changes
REM ==========================================
echo [1/4] Pulling latest from GitHub...
echo.

git pull origin main --rebase --autostash

if errorlevel 1 (
    echo.
    echo [!] Rebasing failed. Trying merge...
    git rebase --abort 2>nul
    git pull origin main --no-rebase
    if errorlevel 1 (
        echo.
        echo [!] Merge conflict detected. Auto-resolving .dockerignore...
        git checkout --ours .dockerignore
        git add .dockerignore
        git commit -m "Resolved merge conflict in .dockerignore"
        echo.
        echo [✓] Conflict resolved.
    )
)

echo.
echo [2/4] Adding all changes...
git add .

echo.
echo [3/4] Committing...
git commit -m "Auto-update: %date% %time%"

echo.
echo [4/4] Pushing to GitHub...
git push origin main

if errorlevel 1 (
    echo.
    echo [ERROR] Push failed. Try again later.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo     ✅ SUCCESS!
echo ==========================================
echo.
echo Your code is now on GitHub.
echo.
pause