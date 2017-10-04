import urllib2
import os


username = 'testss'
server = '@<IP>:'
pathtop = '/auto/artifacts/'
dir = os.listdir(pathtop)

def versionname():
    print "printing all paths of NimOS"
    for directory in dir:
            if directory.startswith('package-dev_rel'):
                    print directory
    pathinput = raw_input("Waiting infput:")
    global path
    path = "/auto/artifacts/" + pathinput + "/latest-successful"


def packagenumber():
    for file in os.listdir(path):
        if file.endswith("-opt.manifest"):
            firstcut = file.replace('xx-', '')
            global package_name
            package_name = firstcut.replace('-opt.manifest', '')
            print package_name


def copyfile():
    update = 'scp ' + path + '/*-opt.update ' + username + server + '/var/www/html/software_updates/'
    os.system(update)

    manifest = 'scp ' + path + '/xx*-opt.manifest ' + username + server + '/tftpboot/boot/manifest-' + package_name
    os.system(manifest)

    initrd = 'scp ' + path + '/usb_install-opt/initrd.img ' + username + server + '/tftpboot/boot/initrd.img-' + package_name
    os.system(initrd)

    vmlinuz = 'scp ' + path + '/usb_install-opt/vmlinuz*-opt ' + username + server + '/tftpboot/boot/vmlinuz-' + package_name
    os.system(vmlinuz)



    #print update
    #print manifest
    #print initrd
    #print vmlinuz



if __name__ == "__main__":
    versionname()
    packagenumber()
    copyfile()