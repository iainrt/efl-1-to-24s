import flet as ft

def home_view(on_league_selected):
    def handle_select(e):
        league = dropdown.value
        if league:
            on_league_selected(league)

    dropdown = ft.Dropdown(
        label="Select League",
        options=[
            ft.dropdown.Option("Championship"),
            # Later add League One, League Two
        ],
    )

    return ft.Column(
        controls=[
            dropdown,
            ft.ElevatedButton("Continue", on_click=handle_select)
        ]
    )
