

Create environment: 
conda env create -f environment.yml

Activate environment: conda activate venv_userautomation

Remove environment: 
conda env remove --name venv_userautomation

Deactivate environment: 
conda deactivate

Check environment:  
conda info --envs

conda activate venv_userautomation

Install packages from requirements.txt fle
pip install -r requirements.txt

Update environment: 
conda env update --name venv_userautomation --file environment.yml


conda env export > environment.yml

Update requirements,txt file from environment
pip freeze > requirements.txt



Docker Compose Troubleshooting:

Stop the process that's using port <port number>: 
If you want to keep using port 8080 for the webserver service, you need to stop the process that's currently using this port. You can find out which process is using port 8080 by running the following command in your terminal:

On Windows:
netstat -ano | findstr :8080

On Unix or MacOS:
lsof -i :8080

These commands will show you the PID of the process that's using port 8080. You can then stop this process using the taskkill command on Windows or the kill command on Unix or MacOS.

This command will show you the PID of the process that's using port 8080
taskkill /PID 12345 /F

Replace 12345 with the PID of your process. The /F option is used to forcefully terminate the process.




