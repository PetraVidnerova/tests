from scoop import futures 

def helloWorld(val):
    return "Hello world %s" % val


if __name__ == "__main__":
    ret_values = list(futures.map(helloWorld, range(16)))
    for x in ret_values:
        print(x)

