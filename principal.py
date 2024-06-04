import flet as ft
def main(page: ft.Page):
    page.title = "Routes Example"
    page.adaptive = True
    page.bgcolor=ft.colors.BLACK

    login = ft.Container(
        
            height=1000,
            bgcolor="#ffffff",
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        margin=ft.margin.only(left=20, right=20, top=15),
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    ft.Image(
                                        src = ('image.png'),
                                        width=200,
                                    )
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ),
                    ft.Container(
                        width=300,
                        margin=ft.margin.only(left=20, right=30, top=35),
                        content=ft.Text(
                            "Registre seu Ponto",
                            color="#000000",
                            text_align="center"
                        )
                    ),
                    ft.Container(
                        width=300,
                        margin=ft.margin.only(left=20, right=20, top=15),
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Matricula",
                                    size=14,
                                    color="#000000",
                                ),
                                ft.TextField(
                                    text_style=ft.TextStyle(
                                        color="#000000",
                                    ),
                                    border_radius=15,
                                    border_color=ft.colors.BLACK,
                                    focused_border_color=ft.colors.ORANGE_700,
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        width=300,
                        margin=ft.margin.only(left=20, right=20, top=5),
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Senha",
                                    size=14,
                                    color="#000000",
                                ),
                                ft.TextField(
                                    text_style=ft.TextStyle(
                                        color="#000000",
                                    ),
                                    password=True,
                                    border_radius=15,
                                    border_color=ft.colors.BLACK,
                                    focused_border_color=ft.colors.ORANGE_700,
                                    can_reveal_password=True
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        width=300,
                        margin=ft.margin.only(left=20, right=20, top=20),
                        content=ft.TextButton(
                            "Acessar",
                            width=300,
                            height=50,
                            on_click=lambda _: page.go("/menu"),
                            style=ft.ButtonStyle(
                                color="#ffffff",
                                bgcolor=ft.colors.BLUE_700,
                            )
                        )
                    ),
                    ft.Container(
                        width=300,
                        content=ft.TextButton(
                            "Esqueceu a senha?",
                            style=ft.ButtonStyle(
                                color="#A9A9A9"
                            )
                        )
                    ),
                    ft.Container(
                        width=300,
                        content=ft.TextButton(
                            "Clique Aqui",
                            width=300,
                            height=50,
                            style=ft.ButtonStyle(
                                color="#0000ff",
                            )
                        )
                    )
                ]
            ),

        )

    # tela de bater ponto
    botao_selecionar=ft.CupertinoSegmentedButton(
            padding=ft.padding.only(top=20),
            selected_index=2,
            click_color=ft.colors.GREEN,
            selected_color='#008000',
            unselected_color=ft.colors.WHITE,
            border_color='#878787',
            on_change=lambda e: print(f"selected_index: {e.data}"),
            controls=[
                ft.Container(
                    padding=ft.padding.symmetric(0, 30),
                    content=ft.Text("CPF", weight=ft.FontWeight.BOLD),
                ),
                ft.Container(
                    padding=ft.padding.symmetric(10, 10),
                    content=ft.Text("MATRICULA", weight=ft.FontWeight.BOLD),
                ),
            ],
        )

    btn_voltar=ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.TextButton(
                        "CONFIRMAR",
                        on_click=lambda _: page.go("/confirmacao"),
                        style=ft.ButtonStyle(
                            color="green",
                            bgcolor=ft.colors.WHITE,

                        )
                    ),
            ]
        )
    )

    header=ft.Container(
        padding=ft.padding.only(top=31),
        height=152,
        bgcolor=ft.colors.WHITE,
        alignment=ft.alignment.center,
        content=ft.Container(
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                    controls=[
                    ft.Text(
                        value='Nome do Usuário',
                        color=ft.colors.BLACK,
                    ),
                    ft.Text(
                        value='13/05/2024',
                        color=ft.colors.BLACK
                    ),
                    botao_selecionar
                ],
            ),
        ]
    )
            
        )
        
        

        
    )

    inputs = ft.Row(
        controls=[
            ft.TextField(hint_text=" ", 
                         width=48, 
                         height=80, 
                         border_radius=ft.border_radius.all(0), 
                         bgcolor=ft.colors.WHITE, 
                         border_width=0, 
                         max_length=1,
                         color=ft.colors.BLACK,
                         autofocus=True
                         ),
            ft.TextField(hint_text=" ", 
                         width=48, 
                         height=80, 
                         border_radius=ft.border_radius.all(0), 
                         bgcolor=ft.colors.WHITE, 
                         border_width=0, 
                         max_length=1,
                         color=ft.colors.BLACK
                         ),
            ft.TextField(hint_text=" ", 
                         width=48, 
                         height=80, 
                         border_radius=ft.border_radius.all(0), 
                         bgcolor=ft.colors.WHITE, 
                         border_width=0, 
                         max_length=1,
                         color=ft.colors.BLACK
                         ),
            ft.TextField(hint_text=" ", 
                         width=48, 
                         height=80, 
                         border_radius=ft.border_radius.all(0), 
                         bgcolor=ft.colors.WHITE, 
                         border_width=0, 
                         max_length=1,
                         color=ft.colors.BLACK
                         ),
        ],
    alignment=ft.MainAxisAlignment.CENTER,
      
    )
    texto = ft.Container(
        alignment=ft.alignment.center,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        value='Digite os 4 primeiros digitos do CPF',
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        width=159,
                        text_align=ft.TextAlign.CENTER,
                    )
                ]
                ),
            bgcolor=ft.colors.BLUE,
    )

    info=ft.Container(
    expand=1,
    content=ft.Column(
        controls=[
            inputs,
            texto,
            btn_voltar  
        ]
    ),
    
    bgcolor=ft.colors.BLUE,
    padding=ft.padding.only(top=80)
)
    
 
    ponto = ft.Container(
        height=1000,
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            
            controls=[
                header,
                info
            ]
        )
        
    )
  

    confirmado =ft.Container(
        alignment=ft.alignment.center,
        height=1000,
        padding=ft.padding.only(top=300),
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value='PONTO REALIZADO COM SUCESSO!!! MEUS PARABÉNS',
                        text_align=ft.TextAlign.CENTER,
                        color=ft.colors.BLACK,
                        size=30,
                        weight=ft.FontWeight.BOLD
                        
                        ),
                ft.TextButton(
                    "SAIR",
                    width=300,
                    height=50,
                    on_click=lambda _: page.go("/"),
                    style=ft.ButtonStyle(
                    color="white",
                    bgcolor=ft.colors.BLUE,
                    )
                    ),
                
            ]
        )
    )

    navManu = ft.Container(
        bgcolor="#0047FF",
        height=50,
        content=ft.Row(
            controls=[
                ft.Icon(name=ft.icons.ARROW_BACK, color=ft.colors.WHITE),
                ft.Text(value="Menu",
                text_align="center",
                color=ft.colors.WHITE,
                width=320,
                )
            ]
        )
    )

    registrar = ft.Container(
        margin = ft.margin.only(top=23),
        alignment=ft.alignment.center,
        content=ft.TextButton(
                'Resgistrar Ponto',
                width=343,
                height=109,
                on_click=lambda _: page.go("/ponto"),
                style=ft.ButtonStyle(
                    color="#ffffff",
                    bgcolor="#0047FF",
                    shape=ft.RoundedRectangleBorder(radius=8),
                    )
                )
    )
    relatorio = ft.Container(
        margin = ft.margin.only(top=23),
        border_radius=ft.border_radius.all(8),
        alignment=ft.alignment.center,
        width=343,
        height=109,
        content=ft.TextButton(
                'Relatório (Histórico)',
                width=343,
                height=109,
                on_click=lambda _: page.go("/ponto"),
                style=ft.ButtonStyle(
                    color="#ffffff",
                    bgcolor="#0047FF",
                    shape=ft.RoundedRectangleBorder(radius=8),
                    )
                )
    )
    sair = ft.Container(
        margin = ft.margin.only(top=23),
        border_radius=ft.border_radius.all(8),
        alignment=ft.alignment.center,
        width=343,
        height=109,
        content=ft.TextButton(
                'Sair',
                width=343,
                height=109,
                on_click=lambda _: page.go("/"),
                style=ft.ButtonStyle(
                    color="#ffffff",
                    bgcolor="#0047FF",
                    shape=ft.RoundedRectangleBorder(radius=8),
                    )
                )
    )

    menu = ft.Container(
        height=1000,
        bgcolor=ft.colors.WHITE,
        alignment=ft.alignment.center,
        content=ft.Column(
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[  
                navManu,
                registrar,
                relatorio,
                sair
            ]
        )
    )

    safeMenu = ft.SafeArea(
        menu
    )



    navHistorico = ft.Container(
        bgcolor="#0047FF",
        height=50,
        content=ft.Row(
            controls=[
                ft.Icon(name=ft.icons.ARROW_BACK, color=ft.colors.WHITE),
                ft.Text(value="Historico",
                text_align="center",
                color=ft.colors.WHITE,
                width=320,
                )
            ]
        )
    )

    funcionarios = [
        {
            'nome': 'João',
            'idade': 30,
            'data': '04/06/2020 - 08:00'
        },
        {
            'nome': 'Maria',
            'idade': 25,
            'data': '04/06/2020 - 08:00'
        },
        {
            'nome': 'Carlos',
            'idade': 35,
            'data': '04/06/2020 - 08:00'
        }
    ]

    historico = ft.Container(
        height=1000,
        bgcolor=ft.colors.WHITE,
        alignment=ft.alignment.center,
        content=ft.Column(
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.alignment.center,
            controls=[  
                ft.Container(
                    margin=ft.margin.only(top=23),
                    border_radius=ft.border_radius.all(8),
                    alignment=ft.alignment.center,
                    width=343,
                    height=109,
                    bgcolor="#0047FF",
                    content=ft.Column(
                        spacing=10,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.alignment.center,
                        controls=[
                            ft.Text(
                                value=f'{funcionario["nome"]}',
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.BOLD,
                                size=20
                                
                            ),
                            ft.Text(
                                value=f'cpf: {funcionario["idade"]}',
                                text_align=ft.TextAlign.CENTER,
                                size=12,
                            ),
                            ft.Text(
                                value=f'{funcionario["data"]}',
                                text_align=ft.TextAlign.CENTER,
                                size=12,
                            )
                        ]
                    )
                ) for funcionario in funcionarios
            ]
        )
    )


    hist = ft.Container(
        height=1000,
        bgcolor=ft.colors.WHITE,
        alignment=ft.alignment.center,
        content=ft.Column(
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[  
                navHistorico,
                historico
                
            ]
        )
    )
    
    safeRelatorio = ft.SafeArea(
        hist
    )


    safeLogin = ft.SafeArea(
        login
    )
    safePonto = ft.SafeArea(
        ponto
    )
    safeConfirmacao = ft.SafeArea(
        confirmado
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    safeLogin
                ],
            )
        )
        if page.route == "/menu":
            page.views.append(
                ft.View(
                    "/menu",
                    [
                        safeMenu
                    ],
                )
            )
        if page.route == "/relacao":
            page.views.append(
                ft.View(
                    "/relacao",
                    [
                        safeRelatorio
                    ],
                )
            )
        page.update()
        page.update()
        if page.route == "/ponto":
            page.views.append(
                ft.View(
                    "/ponto",
                    [
                        safePonto
                    ],
                )
            )
        page.update()
        if page.route == "/confirmacao":
            page.views.append(
                ft.View(
                    "/confirmacao",
                    [
                        safeConfirmacao
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)