import streamlit as st
import requests



def W_MSG(msg, phone):
    url = "https://api.ultramsg.com/instance77439/messages/chat"

    payload = f"token=ae5q0k74f6f9o2ux&to=%2B{phone}&body={msg}"
    payload = payload.encode('utf8').decode('iso-8859-1')
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    requests.request("POST", url, data=payload, headers=headers)


intro ="""<p><h2> Porque cuando más dentro de mis audífonos estaba...  <br>
    ...llegó usted, se trajo su voz y su sonrisa hermosa... <br>
    ...y de ahí en adelante no hubo nada más que quisiera escuchar. <br>
    Se trajo su genio como antídoto para mi ego...<br>
    ...y en contraste, una ternura infinita. <br>
    Se trajo sus besos mágicos, sus caricias y su piel... <br>
    ...y me los dio de a poco <br>
    ...y me dijo que no me acostumbrara a lo bueno. <br>
    Pero Paula me enamoré de sus besos descalzos <br>
    ...esos que terminan en sol saliendo<br>
    ...me enamoré de su respiración y su desnudez temblorosa... <br>
    ...me enamoré de la sensación que me da tomarla de la mano y darle los buenos días con un beso... <br>
    ...me llenó de ilusión el pecho y de calma los días... <br>
    ...me enamoré de la miel que le pone a este desastre que soy. <br>
    Y lo bueno está aún por llegar... <br>
    ...me faltan infinitos caminos por recorrerle a besos en la piel <br>
    ...me quedan infinitas noches por sacarla a bailar <br>
    ...nos quedan todas las tardes para caminar la ciudad y sentarnos a por un café... <br>
    ...nos quedan otras tantas tardes de cine, <br>
    ...tardes de TV y apapachos en el sofá <br>
    ...dias encima de una cama besandonos y dejando el tiempo pasar <br>
    ...viajes, otros dias grises, peleas, sexo de reconciliación <br>
    ...inseguridades por conocer y demonios con los que pelear <br>
    ...juntos.</h2></p>"""


Punchline = """<h2> Y es que con usted todo se me antoja, todo lo quiero... <br>
            ...pero como el mundo hay que comérselo, pero de a pedacitos. <br>
            Hoy le pregunto, como si se lo estuviera susurrando al oido... <br>
            QUIERE SER MI NOVIA?</h2><br><br>"""

ok_si = "La quiero demasiado cielo mío. Quiero estar a su lado en todo lo que queda por venir. Quiero que se apoye en mi en esos dias malos, que me confie sus secretos mas dolorosos y compartir todas sus alegrias. Quiero conocerle cada rincón y alumbrarle cada calle oscura. Quiero que cuando tiemble la tierra se quede conmigi en cama, quiero hacer temblar el continente desnudo con usted en una cama. Las palabras nunca se me van a acabar pa decirle cuanto al adoro, y nunca voy a para de demostrarle cuanto la respeto y me importa. Lo mejor de mis dias siempre es verte pegadita a mi."


st.set_page_config(layout= "centered",
                    page_title = "Do You Want To Be My Girl?",
                    page_icon=":heart")

if "desc_id" not in st.session_state:
    st.session_state.desc_id = 0
if "allow_no_b" not in st.session_state:
    st.session_state.allow_no_b = False

def flag():
    if st.session_state.desc_id == -1:
        st.error("Hey!! No tiene gracia que le des tanto al boton de que no quieres ser mi novia")
        st.session_state.allow_no_b =  True


main = st.container()
with main:
    main.header("Tengo mil maneras de ir a ti:", divider='rainbow')
    main.markdown(intro, unsafe_allow_html=True)
    main.divider()
    main.markdown(Punchline, unsafe_allow_html=True)
    l, c, r = main.columns(3)
    with r:
        si_B = r.button(key= "si", label="SI", on_click=flag(), disabled=st.session_state.allow_no_b)
        no_b = r.button(key= "no",label="NO")
    main.divider()
    if no_b and st.session_state.desc_id == 0:
        W_MSG(msg="jajajaja pendeja, sabia que ibas a poner que NO. Intenta de nuevo.", phone="34670890600")
        st.session_state.desc_id = -1
        st.snow()
    elif si_B and st.session_state.desc_id == -1:
        W_MSG(msg=f"Ya habia dicho que no de primera, pero se lo dejo pasar porque la quiero. {ok_si}", phone="34670890600")
        st.session_state.desc_id = 0
        st.balloons()
    elif si_B and st.session_state.desc_id == 0:
        W_MSG(msg="ok_si", phone="34670890600")
        st.balloons()