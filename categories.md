---
layout: default
---

<h2>CATEGORIES</h2>

<p>
    <ul>
    {% for category in site.categories %}
        <li><a name="{{ category | first }}">{{ category | first }}</a>
            <ul>
                {% for post in category.last %}
                  <li><a href="{{ post.url }}">{{ post.title }}</a></li>
                {% endfor %}
            </ul>
        </li>
    {% endfor %}
    </ul>
</p>
