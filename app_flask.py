from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def mostrar_formulario():
    return render_template('formulario.html')

@app.route('/data-processing', methods=['POST'])
def procesar_formulario():

    datos = request.form

    #Convierte los datos 
    datos_guardar = "\n".join([f"{key}: {value}" for key, value in datos.items()])

    ruta_archivo = os.path.join(os.getcwd(), 'datos_formulario.txt')
    with open(ruta_archivo, 'a') as archivo:
        archivo.write(datos_guardar + "\n\n")

    return "Datos correctamente"

if __name__ == '__main__':
    app.run(debug=True)
    