---
layout: default
---

<h2>TIMEMACHINE</h2>

<p>
    {% for post in site.posts %}
    {% unless post.next %}
      <a href="/year/{{ post.date | date: '%Y' }}">{{ post.date | date: '%Y' }}</a>
    {% else %}
      {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
      {% capture nyear %}{{ post.next.date | date: '%Y' }}{% endcapture %}
      {% if year != nyear %}
        <a href="/year/{{ post.date | date: '%Y' }}">{{ post.date | date: '%Y' }}</a>
      {% endif %}
    {% endunless %}
    {% endfor %}
</p>
