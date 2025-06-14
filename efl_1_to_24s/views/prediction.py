import flet as ft

def prediction_view(page, initial_teams, league, user, on_back):
    print(f"Rendering prediction view for {league}")

    team_order = initial_teams.copy()
    dragged_team = {"name": None}

    list_view = ft.ListView(expand=True, spacing=5, height=600)

    def render_team_list():
        list_view.controls.clear()
        for i, team in enumerate(team_order):
            list_view.controls.append(
                ft.DragTarget(
                    group="teams",
                    on_accept=lambda e, index=i: move_team(index),
                    content=ft.Draggable(
                        group="teams",
                        data=team,
                        content=ft.Container(
                            padding=10,
                            bgcolor=ft.colors.LIGHT_BLUE_50,
                            border=ft.border.all(1, ft.colors.GREY),
                            border_radius=5,
                            content=ft.Row([
                                ft.Text(f"{i+1}", width=30),
                                ft.Text(team)
                            ])
                        ),
                        on_drag_start=lambda e, name=team: on_drag_start(name)
                    )
                )
            )
        page.update()

    def on_drag_start(name):
        dragged_team["name"] = name
        print(f"Dragging: {name}")

    def move_team(target_index):
        if dragged_team["name"] in team_order:
            team_order.remove(dragged_team["name"])
            team_order.insert(target_index, dragged_team["name"])
            render_team_list()

    # Initial render
    render_team_list()

    return ft.Column([
        ft.Text(f"Predict {league} Finishing Order", size=20, weight="bold"),
        ft.Container(height=600, content=list_view, border=ft.border.all(1, ft.colors.GREY)),
        ft.Row([
            ft.ElevatedButton("Save Prediction", on_click=lambda e: print("Save prediction (not implemented yet)")),
            ft.OutlinedButton("Back", on_click=on_back)
        ])
    ])
