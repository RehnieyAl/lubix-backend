from app.services.email.EmailService import send_email


def EmailForgotPassword(to_email: str, code: str):

    subject = "Recuperación de contraseña - Lubix"

    body = f"""
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recuperación de contraseña</title>
</head>

<body style="
    margin:0;
    padding:0;
    background:#0b0f19;
    font-family:Arial, Helvetica, sans-serif;
    color:#ffffff;
">

<table width="100%" cellpadding="0" cellspacing="0">
    <tr>
        <td align="center" style="padding:50px 20px;">

            <table width="650" cellpadding="0" cellspacing="0"
                style="
                    background:#111827;
                    border-radius:18px;
                    overflow:hidden;
                    box-shadow:0 15px 50px rgba(0,0,0,0.6);
                    border:1px solid #1f2937;
                ">

                <!-- HEADER -->
                <tr>
                    <td align="center"
                        style="
                            background:linear-gradient(135deg,#0f172a,#1e3a8a,#065f46);
                            padding:60px 40px;
                        ">

                        <h1 style="
                            margin:0;
                            font-size:44px;
                            letter-spacing:2px;
                            color:#ffffff;
                        ">
                            Lubix
                        </h1>

                        <p style="
                            margin-top:12px;
                            color:#cbd5e1;
                            font-size:15px;
                        ">
                            Recuperación segura de cuenta
                        </p>

                    </td>
                </tr>

                <!-- CONTENT -->
                <tr>
                    <td style="padding:45px;">

                        <h2 style="
                            text-align:center;
                            color:#ffffff;
                            font-size:28px;
                            margin-bottom:15px;
                        ">
                            ¿Olvidaste tu contraseña?
                        </h2>

                        <p style="
                            text-align:center;
                            color:#cbd5e1;
                            font-size:16px;
                            line-height:1.8;
                        ">
                            Hemos recibido una solicitud para restablecer la contraseña de tu cuenta en Lubix.
                        </p>

                        <p style="
                            text-align:center;
                            color:#94a3b8;
                            font-size:14px;
                            line-height:1.8;
                        ">
                            Utiliza el siguiente código para continuar con el proceso:
                        </p>

                        <!-- CODIGO -->
                        <div style="
                            margin-top:30px;
                            background:#0f172a;
                            border:2px solid #1e3a8a;
                            border-radius:14px;
                            padding:30px;
                            text-align:center;
                        ">

                            <span style="
                                font-size:48px;
                                font-weight:bold;
                                color:#38bdf8;
                                letter-spacing:12px;
                                font-family:monospace;
                            ">
                                {code}
                            </span>

                        </div>

                        <!-- INFO -->
                        <div style="
                            margin-top:30px;
                            padding:18px;
                            background:#082f49;
                            border-left:5px solid #38bdf8;
                            border-radius:10px;
                        ">

                            <p style="
                                margin:0;
                                color:#7dd3fc;
                                font-weight:bold;
                            ">
                                ⏳ Código temporal
                            </p>

                            <p style="
                                margin-top:8px;
                                color:#bae6fd;
                                font-size:14px;
                            ">
                                Este código expirará en 10 minutos.
                            </p>

                        </div>

                        <!-- SEGURIDAD -->
                        <div style="
                            margin-top:25px;
                            padding:18px;
                            background:#052e1b;
                            border-left:5px solid #22c55e;
                            border-radius:10px;
                        ">

                            <p style="
                                margin:0;
                                color:#22c55e;
                                font-weight:bold;
                            ">
                                ⚠ Recomendaciones de seguridad
                            </p>

                            <p style="
                                margin-top:8px;
                                color:#86efac;
                                font-size:14px;
                                line-height:1.7;
                            ">
                                No compartas este código con nadie.
                                Lubix nunca solicitará este código por teléfono.
                                Si no realizaste esta solicitud puedes ignorar este correo.
                            </p>

                        </div>

                        <p style="
                            text-align:center;
                            margin-top:35px;
                            color:#64748b;
                            font-size:13px;
                        ">
                            Gracias por confiar en Lubix.
                        </p>

                    </td>
                </tr>

                <!-- FOOTER -->
                <tr>
                    <td align="center"
                        style="
                            background:#0b0f19;
                            padding:25px;
                            font-size:12px;
                            color:#475569;
                        ">
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

    return send_email(to_email, subject, body)