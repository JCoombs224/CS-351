import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'gcode_script')

depth = 7
z_size = 6


def main():
    x = 0
    y = 0
    length = 500
    f = open(filename, "w")

    f.write(f"Z {z_size/(2*depth)}\n")

    f.write(f"G01 {int(x + length)} {y}\n")
    f.write(f"Z {z_size}\n")
    f.write(f"G01 {int(x)} {int(y + length)}\n")
    f.write(f"G01 {int(x - length)} {int(y)}\n")
    f.write(f"Z {z_size/(2*depth)}\n")
    f.write(f"G28\n")
    #f.write(f"G01 0 {y+length}\n")
    #f.write(f"G28\n")

    f.write(f"Z {z_size/(2*depth)}\n")
    f.write(f"G01 {int(x + length)} {y}\n")
    f.write(f"Z {z_size}\n")
    f.write(f"G01 {int(x)} {int(y - length)}\n")
    f.write(f"G01 {int(x - length)} {int(y)}\n")
    f.write(f"Z {z_size/(2*depth)}\n")
    f.write(f"G28\n")
    #f.write(f"G01 0 {y-length}\n")
    #f.write(f"G28\n")

    sierpinksi(f, x, y, z_size/2, length/2, 1)
    #sierpinksi(f, x, y, z_size/2, length, 1)

    #length = int(length/2)
    #f.write(f"G01 {int(x + length*2)} {y}\n")
    #f.write(f"G01 {int(x + length)} {y+length}\n")
    #y = y + length
    #f.write(f"G01 {x} {y}\n")
    #sierpinksi(f, x, y, z_size/4, length/2, 2)

    #f.write(f"G01 {x + length} {y}\n")
    #f.write(f"G01 500 0\n")
    #f.write(f"G28\n")
    #y = 0
    #length = int(500)

    #length = int(length/2)
    #f.write(f"G01 {int(x - length*2)} {y}\n")
    #f.write(f"G01 {int(x - length)} {y-length}\n")
    #y = y - length
    #f.write(f"G01 {x} {y}\n")
    #sierpinksi(f, x, y, z_size/4, -length/2, 2)

    f.close()

def sierpinksi(f, x, y, z, length, count):
    if count >= depth: return

    f.write(f"Z {z_size/(2*depth)}\n")
    f.write(f"G01 {int(x)} {int(y)}\n")
    f.write(f"Z {z}\n")
    f.write(f"G01 {int(x + length)} {int(y + length)}\n")
    f.write(f"G01 {int(x - length)} {int(y + length)}\n")
    f.write(f"G01 {int(x)} {int(y)}\n")
    #f.write(f"G01 {int(x)} {int(y + length)}\n")
    #f.write(f"G01 {int(x)} {int(y)}\n")
    
    f.write(f"Z {z_size/(2*depth)}\n")
    f.write(f"G01 {int(x)} {int(y)}\n")
    f.write(f"Z {z}\n")
    f.write(f"G01 {int(x - length)} {int(y - length)}\n")
    f.write(f"G01 {int(x + length)} {int(y - length)}\n")
    f.write(f"G01 {int(x)} {int(y)}\n")
    #f.write(f"G01 {int(x)} {int(y - length)}\n")
    #f.write(f"G01 {int(x)} {int(y)}\n")

    sierpinksi(f, x - length, y, z/2, length/2, count+1)
    sierpinksi(f, x + length, y, z/2, length/2, count+1)

if __name__ == '__main__':
    main()