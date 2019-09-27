В данной программе мы используем интелектуальный алгоритм для решения задачи коммивояжёра.Решений заключается в итеррационном обходе полносвязного графа муровьями. Каждый муравей строит свой путь по графу, выбор следующей вершины зависит от количества феромона и длины
дуги, эти параметры контролируются константными параметрами "α" и "β" (При α = 0 выбор ближайшего города наиболее вероятен, то есть алгоритм становится жадным. При β = 0 выбор происходит только на основании феромона, что приводит к субоптимальным решениям.). После обхода муравьями проверяется минимальный полученный путь. После каждой итерации феромоны на всех дугах испараются с коэффициентом (1-p), а так же обновляются феромоны на рёбрах, через которые прошли муравьи. Все параметры подбираются опытным методом.
