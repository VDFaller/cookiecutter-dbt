{%- macro clean_text(column) -%}
    {# Normalize common problematic Unicode punctuation and spacing in text fields. #}
    {#- Jinja comments do not fit cleanly inside the mapping, so the values below carry brief intent labels. -#}
    {%- set replacements = {
        "[—\\\\u2011]": ["-", "em-dash, non-breaking hyphen"],
        "[“”]": ["\"", "curly double quotes"],
        "[‘’]": ["\\'", "curly single quotes"],
        "[\\\\u00A0\\\\u202F]": [" ", "nbsp, narrow nbsp"],
        "[\\\\u200B]": ["", "zero-width space"],
    } -%}
    {%- set ns = namespace(expr=column) -%}
    {%- for pattern, replacement in replacements.items() -%}
        {%- set ns.expr = "regexp_replace(" ~ ns.expr ~ ", '" ~ pattern ~ "', '" ~ replacement[0] ~ "')" -%}
    {%- endfor -%}
    {{ ns.expr }}
{%- endmacro -%}
