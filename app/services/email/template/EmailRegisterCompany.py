from app.services.email.EmailService import send_email


def EmailRegisterCompany(
    to_email: str,
    company_name: str,
    company_nit: str
):

    subject = " Solicitud empresarial recibida - Lubix"

    body = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Registro Empresarial</title>
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
Registro empresarial
</p>

</td>
</tr>

<tr>
<td style="padding:45px;">

<h2 style="
text-align:center;
color:#ffffff;
font-size:28px;
margin-bottom:15px;
">
Solicitud recibida correctamente
</h2>

<p style="
text-align:center;
color:#cbd5e1;
font-size:16px;
line-height:1.8;
">
Hemos recibido la información de tu empresa.
</p>

<p style="
text-align:center;
color:#94a3b8;
font-size:14px;
line-height:1.8;
">
Nuestro equipo validará la información antes de aprobar tu empresa.
</p>

<div style="
margin-top:30px;
background:#0f172a;
border:1px solid #1e293b;
border-radius:14px;
padding:25px;
">

<h3 style="
margin-top:0;
color:#38bdf8;
">
 Información registrada
</h3>

<p style="color:#cbd5e1;">
<strong>Empresa:</strong> {company_name}
</p>

<p style="color:#cbd5e1;">
<strong>NIT:</strong> {company_nit}
</p>

</div>

<div style="
margin-top:25px;
padding:18px;
background:#78350f;
border-left:5px solid #f59e0b;
border-radius:10px;
">

<p style="
margin:0;
color:#fbbf24;
font-weight:bold;
">
⏳ Estado actual: En revisión
</p>

<p style="
margin-top:8px;
color:#fde68a;
font-size:14px;
line-height:1.7;
">
Nuestro equipo revisará la información suministrada antes de aprobar la empresa.
</p>

</div>

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
📅 Tiempo estimado
</p>

<p style="
margin-top:8px;
color:#86efac;
font-size:14px;
line-height:1.7;
">
La validación puede tardar hasta 3 días hábiles.
</p>

</div>

<p style="
text-align:center;
margin-top:35px;
color:#64748b;
font-size:13px;
">
Recibirás una nueva notificación cuando el proceso haya finalizado.
</p>

</td>
</tr>

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