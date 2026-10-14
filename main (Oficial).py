productos = []

while True:
    print("\n========================================")
    print("  SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("========================================")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("========================================")
    
    opcion = input("Elegí una opción (1-5): ").strip()
    
    if opcion == "1":
        print("\n--- AGREGAR PRODUCTO ---")
        nombre = input("Nombre del producto: ").strip()
        while nombre == "":
            print("Error: El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre del producto: ").strip()
            
        categoria = input("Categoría del producto: ").strip()
        while categoria == "":
            print("Error: La categoría no puede estar vacía.")
            categoria = input("Ingrese la categoría del producto: ").strip()
            
        precio_str = input("Precio (sin centavos): ").strip()
        while not precio_str.isdigit() or int(precio_str) <= 0:
            print("Error: Ingrese un precio válido (número entero mayor a cero).")
            precio_str = input("Precio (sin centavos): ").strip()
            
        precio = int(precio_str)
        productos.append([nombre, categoria, precio])
        print(f"\n¡Producto '{nombre}' agregado con éxito!")

    elif opcion == "2":
        print("\n--- MOSTRAR PRODUCTOS ---")
        if len(productos) == 0:
            print("Todavía no hay productos cargados.")
        else:
            for i in range(len(productos)):
                p = productos[i]
                print(f"ID {i + 1} | Nombre: {p} | Categoría: {p} | Precio: ${p}")

    elif opcion == "3":
        print("\n--- BUSCAR PRODUCTO ---")
        if len(productos) == 0:
            print("Todavía no hay productos cargados.")
        else:
            busqueda = input("Ingrese el nombre a buscar: ").strip().lower()
            while busqueda == "":
                print("Error: Escriba algún texto para buscar.")
                busqueda = input("Ingrese el nombre a buscar: ").strip().lower()
                
            coincidencias = 0
            for i in range(len(productos)):
                p = productos[i]
                if busqueda in p.lower():
                    print(f"ID {i + 1} | Nombre: {p} | Categoría: {p} | Precio: ${p}")
                    coincidencias += 1
                    
            if coincidencias == 0:
                print("No se encontraron productos con ese nombre.")

    elif opcion == "4":
        print("\n--- ELIMINAR PRODUCTO ---")
        if len(productos) == 0:
            print("Todavía no hay productos cargados.")
        else:
            for i in range(len(productos)):
                p = productos[i]
                print(f"ID {i + 1} | {p} ({p}) - ${p}")
                
            id_eliminar = input("\nNúmero del producto a eliminar: ").strip()
            
            while not id_eliminar.isdigit() or int(id_eliminar) < 1 or int(id_eliminar) > len(productos):
                print(f"Error: Ingrese un número válido entre 1 y {len(productos)}.")
                id_eliminar = input("Número del producto a eliminar: ").strip()
                
            posicion = int(id_eliminar) - 1
            eliminado = productos.pop(posicion)
            print(f"\n¡Se eliminó correctamente el producto '{eliminado}'!")

    elif opcion == "5":
        print("\nGracias por usar el Sistema de Gestión de Productos. ¡Hasta luego!")
        break

    else:
        print("\nOpción no válida. Por favor, elegí un número entre 1 y 5.")
