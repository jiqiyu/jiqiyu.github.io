---
layout: default
---

<h2>TAGS</h2>

{% for tag in site.tags %}
<a href="/tag/{{ tag }}"><code class="highligher-rouge"><nobr>{{ tag }}</nobr></code>&nbsp;</a>{% unless forloop.last %},{% endunless %}
{% endfor %}
