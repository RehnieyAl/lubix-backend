from app.services.email.EmailService import send_email

def EmailLoginCompany(
    to_email: str,
    company_name: str,
    username: str
):

    subject = "Verificación de inicio de sesión en Lubix"

    body = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Verificación de inicio de sesión</title>
</head>

<body style="margin:0; padding:0; background:#0b0f19; font-family:Arial, Helvetica, sans-serif; color:#ffffff;">

<table width="100%" cellpadding="0" cellspacing="0">
    <tr>
        <td align="center" style="padding:50px 20px;">

            <table width="650" cellpadding="0" cellspacing="0"
                style="background:#111827; border-radius:18px; overflow:hidden; box-shadow:0 15px 50px rgba(0,0,0,0.6); border:1px solid #1f2937;">

                <!-- HEADER -->
                <tr>
                    <td align="center" style="background:linear-gradient(135deg,#0f172a,#1e3a8a,#065f46); padding:60px 40px;">
                        <h1 style="margin:0; font-size:42px; color:#ffffff;">Lubix</h1>
                        <p style="margin-top:12px; color:#cbd5e1; font-size:15px;">Acceso seguro para tu empresa</p>
                    </td>
                </tr>

                <!-- CONTENT -->
                <tr>
                    <td style="padding:45px;">
                        <h2 style="text-align:center; color:#ffffff; font-size:26px;">Inicio de sesión verificado</h2>

                        <p style="text-align:center; color:#cbd5e1; font-size:16px; line-height:1.7;">
                            Hola <strong style="color:#22c55e;">{username}</strong>, hemos verificado tu inicio de sesión en la cuenta de <strong style="color:#38bdf8;">{company_name}</strong>.
                        </p>

                        <p style="text-align:center; color:#94a3b8; font-size:14px; line-height:1.7;">
                            El acceso se ha realizado de manera correcta y segura. Ya puedes continuar gestionando tu empresa en Lubix.
                        </p>

                        <!-- STATUS -->
                        <div style="margin-top:30px; padding:18px; background:#052e1b; border-left:5px solid #22c55e; border-radius:10px;">
                            <p style="margin:0; color:#22c55e; font-weight:bold;">✔ Inicio de sesión confirmado</p>
                            <p style="margin-top:8px; color:#86efac; font-size:14px;">Tu sesión empresarial está activa y protegida.</p>
                        </div>

                        <p style="text-align:center; margin-top:35px; color:#64748b; font-size:13px;">Gracias por confiar en Lubix para la gestión de tu empresa</p>
                    </td>
                </tr>

                <!-- FOOTER -->
                <tr>
                    <td align="center" style="background:#0b0f19; padding:25px; font-size:12px; color:#475569;">
                        © 2026 Lubix — Todos los derechos reservados
                    </td>
                </tr>

            </table>
        </td>
    </tr>
</table>

</body>
</html>
"""

    send_email(to_email, subject, body)
