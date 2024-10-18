import streamlit as st

# Sidebar for navigation
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Escolha uma opção", 
                              ["Gerenciamento de Permissões", "Gerenciamento de Grupo e Usuário"])

# Gerenciamento de Permissões
if option == "Gerenciamento de Permissões":
    st.title("Gerenciamento de Permissões")

    owner = list("---")
    group = list("---")
    other = list("---")
    
    st.header("Modificar Permissões")
    st.header("Dono")
    ownerRead = st.checkbox("Leitura")
    ownerWrite = st.checkbox("Gravação")
    ownerExecute = st.checkbox("Execução")
        
        
    st.header("Group")
    groupRead = st.checkbox("Leitura", key=4)
    groupWrite = st.checkbox("Gravação", key=5)
    groupExecute = st.checkbox("Execução", key=6)
        
        
    st.header("Outros")
    otherRead = st.checkbox("Leitura", key=7)
    otherWrite = st.checkbox("Gravação", key=8)
    otherExecute = st.checkbox("Execução", key=9)
    
    path = st.text_input("Caminho do arquivo")
    
    if st.button("Modificar Permissão"):
        if ownerRead:
            owner[0] = "r"
        if ownerWrite:
            owner[1] = "w"
        if ownerExecute:
            owner[2] = "x"
            
        if groupRead:
            group[0] = "r"
        if groupWrite:
            group[1] = "w"
        if groupExecute:
            group[2] = "x"
            
        if otherRead:
            other[0] = "r"
        if otherWrite:
            other[1] = "w"
        if otherExecute:
            other[2] = "x"
        
        owner = "".join(owner)
        group = "".join(group)
        other = "".join(other)
            
        if path:
            st.write("sudo chmod u=" + owner + ",g=" + group + ",o=" + other + " " + path)

# Gerenciamento de Grupo e Usuário
elif option == "Gerenciamento de Grupo e Usuário":
    st.title("Gerenciamento de Grupo e Usuário")

    st.header("Criação de Usuário")
    username = st.text_input("Nome de Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Criar Usuário"):
        if username:
            st.write("sudo adduser " + username)

    st.header("Criação de Grupo")
    group_name = st.text_input("Nome de Grupo")
    if st.button("Criar Grupo"):
        if group_name:
            st.write("sudo addgroup " + group_name)

    st.header("Adicionar Usuário a um Grupo")
    select_user = st.selectbox("Selecionar Usuário", ["User1", "User2", "User3"]) 
    select_group = st.selectbox("Selecionar Grupo", ["Group1", "Group2", "Group3"])
    if st.button("Adicionar Usuário a Grupo"):
        st.write("sudo usermod -aG " + select_group + " " + select_user)
