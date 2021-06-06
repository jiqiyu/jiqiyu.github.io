---
layout: default
---

<h2>CATEGORIES</h2>
<p>
    {% for category in site.categories %}
        {% unless category[0] == '四不像詩歌' %}
            <a href="/category/{{ category[0] }}">
                {{ category[0] }}
            </a>
            <br>
        {% endunless %}
    {% endfor %}
</p>
