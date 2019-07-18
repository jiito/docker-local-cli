# cleanup.py 
def stop(containers, mode):
    print("Stopping:")
    print(containers)
    if len(containers) == 1:
        func[mode](containers[0])
    for container in containers:
        func[mode](container)
    
def graceful(container):
    container.stop()

def kill(container):
    container.kill()

func = {False: graceful, True: kill }