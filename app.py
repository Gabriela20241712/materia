import streamlit as st

# Título
st.title('Mi Primera Aplicación en Streamlit')
st.title('Gabriela Toala')

# Widget text_input
name = st.text_input('Nombres y Apellidos')

#widget Input Box
age = st.number_input('Edad', min_value=0, max_value=100, step=1)

#widget Slider 
month = st.slider('Selecciona un Mes', min_value=1, max_value=12)

#widget Checkbox 
accept_terms = st.checkbox('Acepto los Términos y Condiciones')

#widget Radio Buttons
gender = st.radio('Selecciona tu Género', ('Masculino', 'Femenino', 'Otro'))

#widget Selectbox
country = st.selectbox('Selecciona tu País', ['Argentina', 'Chile', 'Perú', 'México', 'Colombia'])

#widget File Uploader
uploaded_file = st.file_uploader('Cargar un Archivo')

#widget date_input
selected_date = st.date_input('Selecciona una Fecha')

#widget time_input
selected_time = st.time_input('Selecciona una Hora')

#widget button
if st.button('Enviar Información'):
    st.write(f'Gracias, {name}, por enviar tu información.')

#widget Sidebar
st.sidebar.title('Barra Lateral')
st.sidebar.write('Configura algunos elementos aquí:')
st.sidebar.number_input('Edad', min_value=0, max_value=100, step=1, key='sidebar_age')
st.sidebar.slider('Selecciona un Mes', min_value=1, max_value=12, key='sidebar_month')
st.sidebar.selectbox('Selecciona tu País', ['Argentina', 'Chile', 'Perú', 'México', 'Colombia'], key='sidebar_country')

