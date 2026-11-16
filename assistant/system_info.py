import platform,shutil,os
try: import psutil
except ImportError: psutil=None
def get_system_info():
    lines=[f'Operating system: {platform.system()} {platform.release()}',f'Computer: {platform.node()}',f'Processor: {platform.processor() or "Not available"}',f'Python version: {platform.python_version()}']
    if psutil:
        lines += [f'CPU usage: {psutil.cpu_percent(interval=0.4)}%',f'RAM usage: {psutil.virtual_memory().percent}%',f'Available RAM: {psutil.virtual_memory().available/(1024**3):.2f} GB']
        b=psutil.sensors_battery(); lines.append(f'Battery: {b.percent}%' if b else 'Battery: Not available')
    else: lines.append('Install psutil to view CPU, RAM and battery.')
    try:
        total,used,free=shutil.disk_usage(os.path.abspath(os.sep)); lines.append(f'Disk free: {free/(1024**3):.2f} GB')
    except OSError: pass
    return '\n'.join(lines)
