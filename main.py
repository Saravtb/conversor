import flet as ft

def main(page: ft.Page):
    page.title = "Conversor de Temperatura"
    page.theme_mode = "dark"  
    page.padding = 30
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    titulo = ft.Text("Conversor de Temperatura", size=22, weight=ft.FontWeight.W_600)

    direcao = ft.Dropdown(
        label="Direção da conversão",
        value="C → F",
        options=[
            ft.dropdown.Option("C → F"),
            ft.dropdown.Option("F → C"),
        ],
        width=200,
    )

    entrada = ft.TextField(
        label="Digite a temperatura em ºC",
        hint_text="ex.: 23.5",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    resultado = ft.Text(size=18, weight=ft.FontWeight.BOLD)

    def atualizar_label(e=None):
        if direcao.value == "C → F":
            entrada.label = "Digite a temperatura em ºC"
            entrada.hint_text = "ex.: 23.5"
        else:
            entrada.label = "Digite a temperatura em ºF"
            entrada.hint_text = "ex.: 75.2"
        resultado.value = ""
        page.update()

    direcao.on_change = atualizar_label

    def converter(e=None):
        valor_bruto = (entrada.value or "").strip().replace(",", ".")
        try:
            v = float(valor_bruto)
            if direcao.value == "C → F":
                f = (v * 9 / 5) + 32
                resultado.value = f"{v:g} ºC = {f:.2f} ºF"
            else:
                c = (v - 32) * 5 / 9
                resultado.value = f"{v:g} ºF = {c:.2f} ºC"
        except ValueError:
            resultado.value = " Digite um número válido."
        page.update()

    botao = ft.ElevatedButton("Converter", on_click=converter)

    entrada.on_submit = converter

    conteudo = ft.Column(
        [
            titulo,
            ft.Row([direcao], alignment=ft.MainAxisAlignment.CENTER),
            entrada,
            ft.Row([botao], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),
            resultado,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    page.add(conteudo)

    atualizar_label()

ft.app(target=main)
