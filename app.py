import streamlit as st
st.title("SP motors - Aluguel de Carros")
st.sidebar.title("Escolha seu modelo:")
st.sidebar.image("logo.png")

automovel = ["JETTA", "COROLLA", "BMW", "CRETA"]

opcao = st.sidebar.selectbox('Escolha o automóvel que foi alugado', automovel)

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

if opcao == 'BMW':
    diaria = 450

elif opcao == 'JETTA':
    diaria = 400

elif opcao == 'COROLLA':
    diaria = 350

elif opcao == 'CRETA':
    diaria = 350

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dia e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')