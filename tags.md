---
layout: default
---

<h2>TAGS</h2>
{% for tag in site.tags %}
  {% capture tag_name %}{{ tag }}{% endcapture %}
  <a href="/tag/{{ tag_name }}"><code class="highligher-rouge"><nobr>{{ tag_name }}</nobr></code>&nbsp;</a>
{% endfor %}
