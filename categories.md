---
layout: default
---

<h2>CATEGORIES.</h2>
<p>
    {% assign filtered_cats = site.categories | where: '四不像或詩', nil %}
    {% for category in filtered_cats %}
    <a href="/category/{{ filtered_cats[0] }}">
        {{ filtered_cats[0] }}
    </a>
    <br>
    {% endfor %}
</p>
