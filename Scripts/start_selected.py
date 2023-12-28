import os
import multiprocessing
from multiprocessing import Process
import sys

folder_path = r'C:\app\Scripts'
selected_apps = ['head_office.py', 'ilupeju_branch.py', 'suncity.py','index.py','dashboard.py','about.py','sbu1.py','sbu2.py','mararaba.py','kaduna.py','ilupeju_sbu.py']

def start_dash_app(app_file):
    app_path = os.path.join(folder_path, app_file)
    os.system(f'python {app_path}')

if __name__ == '__main__':
    processes = []
    for app_file in selected_apps:
        process = Process(target=start_dash_app, args=(app_file,))
        process.start()
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.join()
