---
layout: default
---

<h2>CATEGORIES</h2>

<p>
    {% for category in site.categories %}
    <a href="/category/{{ category[0] }}">
        {{ category[0] }}
    </a>
    <br>
    {% endfor %}
</p>


