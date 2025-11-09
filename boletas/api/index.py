import flet as ft
import csv

def main(page: ft.Page):
    page.title="BOLETAS DE CALIFICACIONES"
    page.bgcolor= "grey"
    page.window_width= 1600
    page.window_height= 600

    lista_alumnos= ft.Dropdown(
        width=300,
        label="alumnos",
        options=[
            ft.dropdown.Option("dulce maria valadez molina"),
            ft.dropdown.Option("Mateo López"),
            ft.dropdown.Option("María José Hernández"),
            ft.dropdown.Option("Santiago Rodríguez"),
            ft.dropdown.Option("Sofía García"),
            ft.dropdown.Option("Valentina Martínez"),
            ft.dropdown.Option("Sebastián González"),
            ft.dropdown.Option("Regina Pérez"),
            ft.dropdown.Option("Alejandro Sánchez"),
        ],
    )

    esp= ft.Dropdown(
        width=200,
        label= "español",
        options=[ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )
    
    mat= ft.Dropdown(
        width=200,
        label= "matematicas",
        options=[ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )

    ing= ft.Dropdown(
        width=200,
        label= "ingles",
        options=[ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )
    
    hum= ft.Dropdown(
        width=200,
        label= "humanidades",
        options=[ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )
    
    
    emp= ft.Dropdown(
        width=200,
        label= "emplea",
        options=[ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )
    
    
    eco= ft.Dropdown(
        width=200,
        label= "ecosistema",
        options=[ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )
    
    
    apl= ft.Dropdown(
        width=200,
        label= "aplica",
        options=[ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )

    edu= ft.Dropdown(
        width=200,
        label= "educacion fisica",
        options=[ft.dropdown.Option(str(i)) for i in range(10,101,10)]
    )
    
    label_promedio = ft.Text(value="",size=20, width=100,color="red")

    tabla_calificaciones = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Alumno")),
            ft.DataColumn(label=ft.Text("Español")),
            ft.DataColumn(label=ft.Text("Matemáticas")),
            ft.DataColumn(label=ft.Text("Inglés")),
            ft.DataColumn(label=ft.Text("Humanidades")),
            ft.DataColumn(label=ft.Text("Emplea")),
            ft.DataColumn(label=ft.Text("Ecosistema")),
            ft.DataColumn(label=ft.Text("Aplica")),
            ft.DataColumn(label=ft.Text("Educación Física")),
            ft.DataColumn(label=ft.Text("Semáforo")),          # nueva columna
            ft.DataColumn(label=ft.Text("Promedio")),
            ft.DataColumn(label=ft.Text("Eliminar")),  # Nueva columna
        ],
        rows=[]
    )

    def eliminar_fila(e, index):
        tabla_calificaciones.rows.pop(index)
        page.update()

    def calcular_promedio(e):
        alumno = lista_alumnos.value or ""
        if not alumno:
            label_promedio.value = "Selecciona alumno"
            page.update()
            return

        # Evitar duplicados: comprobar si el alumno ya está en la tabla
        for row in tabla_calificaciones.rows:
            cell_val = getattr(row.cells[0].content, "value", "")  # seguridad por si cambia la estructura
            if cell_val == alumno:
                label_promedio.value = "Alumno ya agregado"
                page.update()
                return

        notas = [
            int(esp.value or 0),
            int(mat.value or 0),
            int(ing.value or 0),
            int(hum.value or 0),
            int(emp.value or 0),
            int(eco.value or 0),
            int(apl.value or 0),
            int(edu.value or 0),
        ]

        promedio = sum(notas) / len(notas)
        label_promedio.value = f"{promedio:.2f}"

        # Determinar color del semáforo según el promedio
        if promedio >= 85:
            sem_color = "green"
        elif promedio >= 70:
            sem_color = "yellow"
        else:
            sem_color = "red"

        semaforo_widget = ft.Container(
            width=18,
            height=18,
            bgcolor=sem_color,
            border_radius=9
        )

        # Agregar una nueva fila a la tabla (incluye semáforo)
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(alumno)),
                ft.DataCell(ft.Text(esp.value or "")),
                ft.DataCell(ft.Text(mat.value or "")),
                ft.DataCell(ft.Text(ing.value or "")),
                ft.DataCell(ft.Text(hum.value or "")),
                ft.DataCell(ft.Text(emp.value or "")),
                ft.DataCell(ft.Text(eco.value or "")),
                ft.DataCell(ft.Text(apl.value or "")),
                ft.DataCell(ft.Text(edu.value or "")),
                ft.DataCell(semaforo_widget),                       # celda del semáforo
                ft.DataCell(ft.Text(f"{promedio:.2f}")),
                ft.DataCell(
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color="red",
                        on_click=lambda e, i=len(tabla_calificaciones.rows): eliminar_fila(e, i)
                    )
                ),
            ]
        )
        tabla_calificaciones.rows.append(nueva_fila)
        page.update()

    # Función para borrar la tabla (definida antes de crear los botones)
    def borrar_tabla(e):
        tabla_calificaciones.rows.clear()
        label_promedio.value = ""
        page.update()

    def exportar_csv(e):
        with open('calificaciones.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escribir encabezados
            writer.writerow(["Alumno", "Español", "Matemáticas", "Inglés", "Humanidades", 
                        "Emplea", "Ecosistema", "Aplica", "Educación Física", "Promedio"])
            
            # Escribir datos de la tabla
            for row in tabla_calificaciones.rows:
                # Obtener valores, excluyendo el semáforo
                row_data = []
                for cell in row.cells:
                    # Si es un Text widget, obtener su valor
                    if isinstance(cell.content, ft.Text):
                        row_data.append(cell.content.value)
                    # Si es un Container (semáforo), saltar
                    elif isinstance(cell.content, ft.Container):
                        continue
                writer.writerow(row_data)

        label_promedio.value = "Datos exportados a calificaciones.csv"
        page.update()

    # Botón para calcular el promedio
    boton_calcular = ft.ElevatedButton(text="Calcular Promedio", on_click=calcular_promedio)

    # Botón para borrar la tabla
    boton_borrar = ft.ElevatedButton(text="Borrar Tabla", bgcolor="red", color="white", on_click=borrar_tabla)

    # Botón para exportar a CSV
    boton_exportar_csv = ft.ElevatedButton(text="Exportar CSV", on_click=exportar_csv)

    fila_dropdowns= ft.Row(
        [
            lista_alumnos,
            esp,
            mat,
            ing,
            hum,
            emp,
            eco,
            apl,
            edu,
            label_promedio
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

    fila_boton=ft.Row(
        [boton_calcular, boton_borrar, boton_exportar_csv],
        alignment=ft.MainAxisAlignment.CENTER
    )
    

    page.add(
        ft.Column(
            [
                fila_dropdowns,
                fila_boton,

                tabla_calificaciones
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )
app = lambda: ft.app(target=main, view=ft.WEB_BROWSER, port=8080)

if __name__ == "__main__":
    app()
