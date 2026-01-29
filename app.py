✔ st.write() – показва текст
✔ st.text_input() – текстов отговор
✔ st.number_input() – число
✔ if / else – проверка
✔ st.button() – действие
Пример – въпрос и отговор
import streamlit as st
st.write("Как се казваш?")
name = st.text_input("Въведи името си")
if name:
  st.write("Здравей,", name)

Поянсения:
text_input → поле за въвеждане
if name: → проверява дали има въведен текст
Пример с число и проверка (възраст)
import streamlit as st
st.title("Проверка на възраст")
age = st.number_input("На колко години си?", min_value=0, max_value=120)
if age >= 18:
  st.success("Ти си пълнолетен.")
elif age >=0:
  st.warning("Ти не си пълнолетен.")

Допълнение:
number_input → въвеждане на число
if / elif →проверка (като if–else)
Пример с избор (да / не)
import streamlit as st
st.title("Въпрос")
answer = st.radio(
  "Обичаш ли програмирането?",
  ("да", "не")
)
if answer == "да":
  st.write("Страхотно! Продължавай ")
else:
  st.write("Няма проблем, ще го харесаш ")
radio → избор между варианти (без грешно въвеждане)
Мини тест (въпрос + проверка)
import streamlit as st
st.title("Мини тест")
answer = st.number_input("Колко е 2 + 2?", step=1)
if st.button("Провери"):
  if answer == 4:
    st.success("Вярно! Браво")
  else:
    st.error("Грешно. Опитай пак ")
button → проверката става само при натискане

Пример:
import streamlit as st
st.title("Малка програма с въпрос")
name = st.text_input("Как се казваш?")
age = st.number_input("На колко години си?", min_value=0, max_value=120)
if st.button("Провери"):
  st.write("Здравей,", name)
  if age >= 18:
    st.success("Ти си пълнолетен.")
  else:
    st.warning("Ти не си пълнолетен.")

Упражнение 1
Направете програма, която:
пита „Обичаш ли Python?“
ако отговорът е „да“ → „Супер!“
ако е „не“ → „Ще го харесаш!“

Упражнение 2
Програма, която:
пита за число
ако е по-голямо от 10 → „Голямо число“
иначе → „Малко число“

Упражнение 3 (по-трудно)
Мини тест:
въпрос: „Колко е 5 × 5?“
бутон „Провери“
вярно → зелено съобщение
грешно → червено съобщение

