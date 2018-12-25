---
layout: default
---

<h2>TIMEMACHINE</h2>

<p>
    {% for post in site.posts %}
    {% unless post.next %}
      <a href="/year/{{ post.date | date: '%Y %b' }}">{{ post.date | date: '%Y %b' }}</a>
    {% else %}
      {% capture year %}{{ post.date | date: '%Y %b' }}{% endcapture %}
      {% capture nyear %}{{ post.next.date | date: '%Y %b' }}{% endcapture %}
      {% if year != nyear %}
        <a href="/year/{{ post.date | date: '%Y %b' }}">{{ post.date | date: '%Y %b' }}</a>
      {% endif %}
    {% endunless %}
    {% endfor %}
</p>
