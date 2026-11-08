import streamlit as st

st.title("Mi primera aplicación de Streamlit")
st.subheader("¡Hola, Streamlit!")


# Inicio de la barra lateral
st.sidebar.title("Mi primera barra lateral de Streamlit")
st.sidebar.text("¡Hola, Barra Lateral!")

#     ÁREA PRINCIPAL    
st.text("Esta es una aplicación simple")
st.image("https://researchers.uss.cl/skin/footerIcon/", width=250)

# Botón del área principal
if st.button("Haz clic"):
    st.write("¡Botón presionado!")

# Campo de texto del área principal
nombre_texto = st.text_input("Escribe algo:")
st.write(f"Escribiste: {nombre_texto}")


#     BARRA LATERAL    
st.sidebar.text("Esto es una barra lateral")
st.sidebar.image("https://researchers.uss.cl/skin/footerIcon/", width=200)

# Botón de la barra lateral
if st.sidebar.button("Haz clic pero en la barra lateral"):
    st.sidebar.write("¡Botón de la barra presionado!")

# Campo de texto de la barra lateral
texto_barra = st.sidebar.text_input("Escribe algo en la barra:")
st.sidebar.write(f"Escribiste en la barra: {texto_barra}")
