def body(files : list, html : str = None, body : str = None) -> str:
    if html is None:
        html = f"""<html>
    <head><style>
    table {{
    width: 100%;
    border-collapse: collapse;
    }}
    th, td {{
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
    font-family: monospace;
    }}
    th {{
    background-color: #f2f2f2;
    }}
    </style></head>
    <body>
    <p>{body.replace('\n', '<br>')}</p>
    <h3>Resumen de archivos</h3>
    <table>
    <tr>
    <th>Archivo</th><th>Existe</th><th>Tamaño (bytes)</th><th>Creado</th><th>Modificado</th>
    </tr>
    """

    for file in files:
        html += f"<tr><td>{file.file_path}</td><td>{'✅' if file.exists else '❌'}</td>" \
                f"<td>{file.size}</td><td>{file.creation_date or '-'}</td>" \
                f"<td>{file.last_modification_date or '-'}</td></tr>"

    html += "</table></body></html>"
    return html