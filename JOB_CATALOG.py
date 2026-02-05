JOB_CATALOG = [
    {
        "job_id": "echo",
        "description": "Devuelve exactamente el mensaje entregado, sin modificaciones.",
        "parameters": {
            "message": {"type": "string", "description": "Texto a devolver tal cual."}
        },
    },
    {
        "job_id": "add_numbers",
        "description": "Suma dos números reales y devuelve el resultado.",
        "parameters": {
            "a": {"type": "number", "description": "Primer número."},
            "b": {"type": "number", "description": "Segundo número."},
        },
    },
    {
        "job_id": "get_system_time",
        "description": "Obtiene la fecha y hora actual del sistema.",
        "parameters": {},
    },
    {
        "job_id": "delay_job",
        "description": "Ejecuta otro job después de un retraso especificado.",
        "parameters": {"delay_seconds": {"type": "number"}, "job": {"type": "job"}},
    },
]
