# Prompt user to enter pie and radius of sphere and calculate the volume.
def volume_of_sphere(pie, r):
    volume = (4 / 3 * pie * r ** 3)
    return volume


pie = float(input("Enter pie: "))
r = int(input("Enter the radius of a sphere: "))
print(volume_of_sphere(pie, r))
