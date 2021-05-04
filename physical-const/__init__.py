import math

class constant():
	def __init__(self,name,symbol,value,unit):
		self.name = name
		self.symbol = symbol
		self.value = value
		self.unit = unit

speed_of_light = constant('speed of light in vacuo','𝑐', 3.00*10**8,'ms^-1')
permeability_of_free_space = constant('permeability of free space','𝜇',4*math.pi*10**-7,'Hm^-1')
permittivity_of_free_space = constant('permittivity of free space','𝜀',8.85*10**-12,'Fm^-1')
electron_charge = constant('magnitude of the charge of electron', '𝑒',1.6*10**-19, 'C')
Planck_const = constant('the Planck constant', 'ℎ', 6.63*10**-34, 'Js')
grav_const = constant('gravitational constant', '𝐺', 6.67*10**-11,'Nm2kg^-2')
Avogadro_const = constant('the Avogadro constant', '𝑁A', 6.02*10**23, 'mol^-1')
mol_gas_const = constant('molar gas constant', '𝑅', 8.31, 'JK^-1mol^-1')
Boltzmann_const = constant('the Boltzmann constant', '𝑘', 1.38*10**-23, 'JK^-1')
Stefan_const = constant('the Stefan constant', 'σ', 5.67*10**-8, 'Wm^-2K^-4')
Wien_const = constant('the Wien constant', '𝛼', 2.90*10**-3, 'mK')
electron_mass = constant('electron rest mass(equivalent to 5.5×10^-4 u)', '𝑚e', 9.11*10**-31, 'kg')
electron_charge_mass = constant('electron charge/mass ratio', '𝑒𝑚e', 1.76*10**11, 'Ckg^-1')
proton_mass = constant('proton rest mass(equivalent to 1.00728u)', '𝑚p', 1.6733333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333*10**-27, 'kg')
proton_charge_mass = constant('proton charge/mass ratio', '𝑒𝑚p', 9.58*10**7, 'Ckg^-1')
neutron_mass = constant('neutron rest mass(equivalent to 1.00867u)', '𝑚n', 1.675555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555*10**-27, 'kg')
gravitational_field_strength = constant('gravitational field strength', '𝑔', 9.81, 'Nkg^-1')
acceleration_due_to_gravity = constant('acceleration due to gravity', '𝑔', 9.81, 'ms^-2')
atomic_mass = constant('atomic mass unit(1u is equivalent to 931.5MeV)', 'u', 1.661*10**-27, 'kg')


if __name__ == '__main__':
	print(speed_of_light.name,speed_of_light.symbol,speed_of_light.value,speed_of_light.unit)
