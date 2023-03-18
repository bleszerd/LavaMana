import os
import shutil
import sys

SOURCE_PROTO_PATH = 'lavanda-manager/proto'
SOURCE_SERVICE_PATH = 'lavanda-manager/services'

# List of microservices to push proto/service files
microservices = [
    {
        "name": "authentication",
    },
    {
        "name": "user",
    },
]


def push_to_microservices(args):
    flag = args["flag"]
    flagArg = args["flagArg"]

    for microservice in microservices:
        microserviceName = microservice["name"]
        if (flag != None and flag == "--i" and microserviceName in flagArg):
            continue

        dest_dir_proto = f'lavanda-{microserviceName}/src/proto'
        dest_dir_services = f'lavanda-{microserviceName}/src/services'

        shutil.copytree(SOURCE_PROTO_PATH, dest_dir_proto, dirs_exist_ok=True)
        shutil.copytree(
            SOURCE_SERVICE_PATH,
            dest_dir_services, dirs_exist_ok=True,
        )


def clean_microservices():
    for microservice in microservices:
        microserviceName = microservice["name"]

        dir_proto = f'lavanda-{microserviceName}/src/proto'
        dir_services = f'lavanda-{microserviceName}/src/services'

        protoFiles = os.listdir(dir_proto)
        serviceFolders = os.listdir(dir_services)

        for protoFile in protoFiles:
            if protoFile.endswith(".proto"):
                os.remove(f'{dir_proto}/{protoFile}')

        for serviceFolder in serviceFolders:
            shutil.rmtree(f'{dir_services}/{serviceFolder}')


def get_command_args():
    pullCommand = len(sys.argv)

    command = sys.argv[1]
    flag = None
    flagArg = None

    if (pullCommand > 2):
        flag = sys.argv[2]
        flagArg = sys.argv[3].split("+")

    return {"command": command, "flag": flag, "flagArg": flagArg}


def main():
    commandArgs = get_command_args()

    match commandArgs["command"]:
        case "pull":
            push_to_microservices(commandArgs)
        case "clean":
            clean_microservices()


if __name__ == "__main__":
    main()
