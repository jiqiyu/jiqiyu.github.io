---
layout: default
---

<h2>TAGS</h2>

<p>
    {% for tag in site.tags %}
    <!-- Here's a hack to generate a "tag cloud" where the size of
    the word is directly proportional to the number of posts with
    that tag. -->
    <a href="/tag/{{ tag[0] }}"
    style="font-size: {{ tag[1] | size | times: 2 | plus: 10 }}px">
        {{ tag[0] }} |
    </a>
    {% endfor %}
</p>
