from pyrsistent import b


def processCmd(cmd):
    cmd_name = ''
    para_list = []
    new_cmd = cmd.replace(' ','',)   # remove space
    para_num = new_cmd.count('/')
    if para_num == 0:
        cmd_name = new_cmd
    else:
        cmd_list = new_cmd.split('/')
        cmd_name = cmd_list[0]
        para_list = cmd_list[1: -1]
        para_list.append(cmd_list[-1])
    return cmd_name, para_list
