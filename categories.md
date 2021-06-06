---
layout: default
---

<h2>CATEGORIES.</h2>
<p>
    {% assign myCats = ['四不像或詩歌', '四不像或小说', '杂', '在別處', '許願池'] %}
    {% for category in myCats %} <!-- site.categories -->
    <a href="/category/{{ myCats[0] }}">
        {{ myCats[0] }}
    </a>
    <br>
    {% endfor %}
</p>
