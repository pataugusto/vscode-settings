import subprocess

print('Script start')

with open('extensions.txt', 'r') as f:
    extensions = [line.strip() for line in f]

for extension in extensions:
	p = subprocess.Popen(['powershell.exe', 'code', '--install-extension', extension], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(f'Installing extension: {extension}')
	
	stdout, stderr = p.communicate()

	result = stdout.decode()
	print(f'{result}')

	if p.returncode != 0:
		print("Exception while running powershell command")
		print(f'stdout: {stdout}')
		print(f'stderr: {stderr}')


print('Script finished')
