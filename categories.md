---
layout: default
---

<h2>CATEGORIES.</h2>
<p>
    {% assign filtered_cats = site.categories | where: '四不像詩歌', nil %}
    {% for category in filtered_cats %}
    <a href="/category/{{ category[0] }}">
        {{ category[0] }}
    </a>
    <br>
    {% endfor %}
</p>
