import win32com.client as win32


def enviar_email(destino: str, assunto: str, body: str):
    """
    Este código envia um e-mail simples, ou seja, sem anexos.
    Para utilizar este código, você deve ter o app do outlook em seu
    windows.

    :destino: coloque o endereço de email
    :assunto: coloque seu assunto/subject
    :body: coloque seu corpo do email
    """

    # criar a integração com o outlook
    outlook = win32.Dispatch('outlook.application')

    # criar um email
    email = outlook.CreateItem(0)

    # configurar as informações do seu e-mail
    email.To = destino
    email.Subject = assunto
    email.HTMLBody = f"""
    <p>{body}</p>

    """

    email.Send()
    print("Email Enviado")