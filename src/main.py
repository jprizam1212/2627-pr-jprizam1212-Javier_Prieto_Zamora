
def formatear_nombre(nombre: str, apellido1: str, apellido2: sorted) -> str:
	""" Descripcion de la funcionalidad

	:param nombre: descripcion del parametro de entrada
	:param apellido1: descripcion del parametro de entrada
	:param apellido2: descripcion del parametro de entrada
	:retur:  lo que devuelve la funcion
	"""
	return nombre.strip().title() + "" + apellido1.strip().title() + "" +apellido2.strip().title()

def main():

	nombre: str = input()
	apellido1: str = input()
	apellido2: str = input()

	nombre_completo = formatear_nombre(nombre, apellido1, apellido2)

	print(nombre_completo)


if __name__ == "__main__":
	main()
