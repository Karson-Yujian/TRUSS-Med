---
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- mteb
model-index:
- name: stella-base-en-v2
  results:
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (en)
      config: en
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 77.19402985074628
    - type: ap
      value: 40.43267503017359
    - type: f1
      value: 71.15585210518594
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_polarity
      name: MTEB AmazonPolarityClassification
      config: default
      split: test
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
    metrics:
    - type: accuracy
      value: 93.256675
    - type: ap
      value: 90.00824833079179
    - type: f1
      value: 93.2473146151734
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (en)
      config: en
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 49.612
    - type: f1
      value: 48.530785631574304
  - task:
      type: Retrieval
    dataset:
      type: arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 37.411
    - type: map_at_10
      value: 52.673
    - type: map_at_100
      value: 53.410999999999994
    - type: map_at_1000
      value: 53.415
    - type: map_at_3
      value: 48.495
    - type: map_at_5
      value: 51.183
    - type: mrr_at_1
      value: 37.838
    - type: mrr_at_10
      value: 52.844
    - type: mrr_at_100
      value: 53.581999999999994
    - type: mrr_at_1000
      value: 53.586
    - type: mrr_at_3
      value: 48.672
    - type: mrr_at_5
      value: 51.272
    - type: ndcg_at_1
      value: 37.411
    - type: ndcg_at_10
      value: 60.626999999999995
    - type: ndcg_at_100
      value: 63.675000000000004
    - type: ndcg_at_1000
      value: 63.776999999999994
    - type: ndcg_at_3
      value: 52.148
    - type: ndcg_at_5
      value: 57.001999999999995
    - type: precision_at_1
      value: 37.411
    - type: precision_at_10
      value: 8.578
    - type: precision_at_100
      value: 0.989
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 20.91
    - type: precision_at_5
      value: 14.908
    - type: recall_at_1
      value: 37.411
    - type: recall_at_10
      value: 85.775
    - type: recall_at_100
      value: 98.86200000000001
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 62.731
    - type: recall_at_5
      value: 74.53800000000001
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-p2p
      name: MTEB ArxivClusteringP2P
      config: default
      split: test
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
    metrics:
    - type: v_measure
      value: 47.24219029437865
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-s2s
      name: MTEB ArxivClusteringS2S
      config: default
      split: test
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
    metrics:
    - type: v_measure
      value: 40.474604844291726
  - task:
      type: Reranking
    dataset:
      type: mteb/askubuntudupquestions-reranking
      name: MTEB AskUbuntuDupQuestions
      config: default
      split: test
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
    metrics:
    - type: map
      value: 62.720542706366054
    - type: mrr
      value: 75.59633733456448
  - task:
      type: STS
    dataset:
      type: mteb/biosses-sts
      name: MTEB BIOSSES
      config: default
      split: test
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
    metrics:
    - type: cos_sim_pearson
      value: 86.31345008397868
    - type: cos_sim_spearman
      value: 85.94292212320399
    - type: euclidean_pearson
      value: 85.03974302774525
    - type: euclidean_spearman
      value: 85.88087251659051
    - type: manhattan_pearson
      value: 84.91900996712951
    - type: manhattan_spearman
      value: 85.96701905781116
  - task:
      type: Classification
    dataset:
      type: mteb/banking77
      name: MTEB Banking77Classification
      config: default
      split: test
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
    metrics:
    - type: accuracy
      value: 84.72727272727273
    - type: f1
      value: 84.29572512364581
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-p2p
      name: MTEB BiorxivClusteringP2P
      config: default
      split: test
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
    metrics:
    - type: v_measure
      value: 39.55532460397536
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-s2s
      name: MTEB BiorxivClusteringS2S
      config: default
      split: test
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
    metrics:
    - type: v_measure
      value: 35.91195973591251
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 32.822
    - type: map_at_10
      value: 44.139
    - type: map_at_100
      value: 45.786
    - type: map_at_1000
      value: 45.906000000000006
    - type: map_at_3
      value: 40.637
    - type: map_at_5
      value: 42.575
    - type: mrr_at_1
      value: 41.059
    - type: mrr_at_10
      value: 50.751000000000005
    - type: mrr_at_100
      value: 51.548
    - type: mrr_at_1000
      value: 51.583999999999996
    - type: mrr_at_3
      value: 48.236000000000004
    - type: mrr_at_5
      value: 49.838
    - type: ndcg_at_1
      value: 41.059
    - type: ndcg_at_10
      value: 50.573
    - type: ndcg_at_100
      value: 56.25
    - type: ndcg_at_1000
      value: 58.004
    - type: ndcg_at_3
      value: 45.995000000000005
    - type: ndcg_at_5
      value: 48.18
    - type: precision_at_1
      value: 41.059
    - type: precision_at_10
      value: 9.757
    - type: precision_at_100
      value: 1.609
    - type: precision_at_1000
      value: 0.20600000000000002
    - type: precision_at_3
      value: 22.222
    - type: precision_at_5
      value: 16.023
    - type: recall_at_1
      value: 32.822
    - type: recall_at_10
      value: 61.794000000000004
    - type: recall_at_100
      value: 85.64699999999999
    - type: recall_at_1000
      value: 96.836
    - type: recall_at_3
      value: 47.999
    - type: recall_at_5
      value: 54.376999999999995
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 29.579
    - type: map_at_10
      value: 39.787
    - type: map_at_100
      value: 40.976
    - type: map_at_1000
      value: 41.108
    - type: map_at_3
      value: 36.819
    - type: map_at_5
      value: 38.437
    - type: mrr_at_1
      value: 37.516
    - type: mrr_at_10
      value: 45.822
    - type: mrr_at_100
      value: 46.454
    - type: mrr_at_1000
      value: 46.495999999999995
    - type: mrr_at_3
      value: 43.556
    - type: mrr_at_5
      value: 44.814
    - type: ndcg_at_1
      value: 37.516
    - type: ndcg_at_10
      value: 45.5
    - type: ndcg_at_100
      value: 49.707
    - type: ndcg_at_1000
      value: 51.842
    - type: ndcg_at_3
      value: 41.369
    - type: ndcg_at_5
      value: 43.161
    - type: precision_at_1
      value: 37.516
    - type: precision_at_10
      value: 8.713
    - type: precision_at_100
      value: 1.38
    - type: precision_at_1000
      value: 0.188
    - type: precision_at_3
      value: 20.233999999999998
    - type: precision_at_5
      value: 14.280000000000001
    - type: recall_at_1
      value: 29.579
    - type: recall_at_10
      value: 55.458
    - type: recall_at_100
      value: 73.49799999999999
    - type: recall_at_1000
      value: 87.08200000000001
    - type: recall_at_3
      value: 42.858000000000004
    - type: recall_at_5
      value: 48.215
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 40.489999999999995
    - type: map_at_10
      value: 53.313
    - type: map_at_100
      value: 54.290000000000006
    - type: map_at_1000
      value: 54.346000000000004
    - type: map_at_3
      value: 49.983
    - type: map_at_5
      value: 51.867
    - type: mrr_at_1
      value: 46.27
    - type: mrr_at_10
      value: 56.660999999999994
    - type: mrr_at_100
      value: 57.274
    - type: mrr_at_1000
      value: 57.301
    - type: mrr_at_3
      value: 54.138
    - type: mrr_at_5
      value: 55.623999999999995
    - type: ndcg_at_1
      value: 46.27
    - type: ndcg_at_10
      value: 59.192
    - type: ndcg_at_100
      value: 63.026
    - type: ndcg_at_1000
      value: 64.079
    - type: ndcg_at_3
      value: 53.656000000000006
    - type: ndcg_at_5
      value: 56.387
    - type: precision_at_1
      value: 46.27
    - type: precision_at_10
      value: 9.511
    - type: precision_at_100
      value: 1.23
    - type: precision_at_1000
      value: 0.136
    - type: precision_at_3
      value: 24.096
    - type: precision_at_5
      value: 16.476
    - type: recall_at_1
      value: 40.489999999999995
    - type: recall_at_10
      value: 73.148
    - type: recall_at_100
      value: 89.723
    - type: recall_at_1000
      value: 97.073
    - type: recall_at_3
      value: 58.363
    - type: recall_at_5
      value: 65.083
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 26.197
    - type: map_at_10
      value: 35.135
    - type: map_at_100
      value: 36.14
    - type: map_at_1000
      value: 36.216
    - type: map_at_3
      value: 32.358
    - type: map_at_5
      value: 33.814
    - type: mrr_at_1
      value: 28.475
    - type: mrr_at_10
      value: 37.096000000000004
    - type: mrr_at_100
      value: 38.006
    - type: mrr_at_1000
      value: 38.06
    - type: mrr_at_3
      value: 34.52
    - type: mrr_at_5
      value: 35.994
    - type: ndcg_at_1
      value: 28.475
    - type: ndcg_at_10
      value: 40.263
    - type: ndcg_at_100
      value: 45.327
    - type: ndcg_at_1000
      value: 47.225
    - type: ndcg_at_3
      value: 34.882000000000005
    - type: ndcg_at_5
      value: 37.347
    - type: precision_at_1
      value: 28.475
    - type: precision_at_10
      value: 6.249
    - type: precision_at_100
      value: 0.919
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 14.689
    - type: precision_at_5
      value: 10.237
    - type: recall_at_1
      value: 26.197
    - type: recall_at_10
      value: 54.17999999999999
    - type: recall_at_100
      value: 77.768
    - type: recall_at_1000
      value: 91.932
    - type: recall_at_3
      value: 39.804
    - type: recall_at_5
      value: 45.660000000000004
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 16.683
    - type: map_at_10
      value: 25.013999999999996
    - type: map_at_100
      value: 26.411
    - type: map_at_1000
      value: 26.531
    - type: map_at_3
      value: 22.357
    - type: map_at_5
      value: 23.982999999999997
    - type: mrr_at_1
      value: 20.896
    - type: mrr_at_10
      value: 29.758000000000003
    - type: mrr_at_100
      value: 30.895
    - type: mrr_at_1000
      value: 30.964999999999996
    - type: mrr_at_3
      value: 27.177
    - type: mrr_at_5
      value: 28.799999999999997
    - type: ndcg_at_1
      value: 20.896
    - type: ndcg_at_10
      value: 30.294999999999998
    - type: ndcg_at_100
      value: 36.68
    - type: ndcg_at_1000
      value: 39.519
    - type: ndcg_at_3
      value: 25.480999999999998
    - type: ndcg_at_5
      value: 28.027
    - type: precision_at_1
      value: 20.896
    - type: precision_at_10
      value: 5.56
    - type: precision_at_100
      value: 1.006
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: precision_at_3
      value: 12.231
    - type: precision_at_5
      value: 9.104
    - type: recall_at_1
      value: 16.683
    - type: recall_at_10
      value: 41.807
    - type: recall_at_100
      value: 69.219
    - type: recall_at_1000
      value: 89.178
    - type: recall_at_3
      value: 28.772
    - type: recall_at_5
      value: 35.167
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 30.653000000000002
    - type: map_at_10
      value: 41.21
    - type: map_at_100
      value: 42.543
    - type: map_at_1000
      value: 42.657000000000004
    - type: map_at_3
      value: 38.094
    - type: map_at_5
      value: 39.966
    - type: mrr_at_1
      value: 37.824999999999996
    - type: mrr_at_10
      value: 47.087
    - type: mrr_at_100
      value: 47.959
    - type: mrr_at_1000
      value: 48.003
    - type: mrr_at_3
      value: 45.043
    - type: mrr_at_5
      value: 46.352
    - type: ndcg_at_1
      value: 37.824999999999996
    - type: ndcg_at_10
      value: 47.158
    - type: ndcg_at_100
      value: 52.65
    - type: ndcg_at_1000
      value: 54.644999999999996
    - type: ndcg_at_3
      value: 42.632999999999996
    - type: ndcg_at_5
      value: 44.994
    - type: precision_at_1
      value: 37.824999999999996
    - type: precision_at_10
      value: 8.498999999999999
    - type: precision_at_100
      value: 1.308
    - type: precision_at_1000
      value: 0.166
    - type: precision_at_3
      value: 20.308
    - type: precision_at_5
      value: 14.283000000000001
    - type: recall_at_1
      value: 30.653000000000002
    - type: recall_at_10
      value: 58.826
    - type: recall_at_100
      value: 81.94
    - type: recall_at_1000
      value: 94.71000000000001
    - type: recall_at_3
      value: 45.965
    - type: recall_at_5
      value: 52.294
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 26.71
    - type: map_at_10
      value: 36.001
    - type: map_at_100
      value: 37.416
    - type: map_at_1000
      value: 37.522
    - type: map_at_3
      value: 32.841
    - type: map_at_5
      value: 34.515
    - type: mrr_at_1
      value: 32.647999999999996
    - type: mrr_at_10
      value: 41.43
    - type: mrr_at_100
      value: 42.433
    - type: mrr_at_1000
      value: 42.482
    - type: mrr_at_3
      value: 39.117000000000004
    - type: mrr_at_5
      value: 40.35
    - type: ndcg_at_1
      value: 32.647999999999996
    - type: ndcg_at_10
      value: 41.629
    - type: ndcg_at_100
      value: 47.707
    - type: ndcg_at_1000
      value: 49.913000000000004
    - type: ndcg_at_3
      value: 36.598000000000006
    - type: ndcg_at_5
      value: 38.696000000000005
    - type: precision_at_1
      value: 32.647999999999996
    - type: precision_at_10
      value: 7.704999999999999
    - type: precision_at_100
      value: 1.242
    - type: precision_at_1000
      value: 0.16
    - type: precision_at_3
      value: 17.314
    - type: precision_at_5
      value: 12.374
    - type: recall_at_1
      value: 26.71
    - type: recall_at_10
      value: 52.898
    - type: recall_at_100
      value: 79.08
    - type: recall_at_1000
      value: 93.94
    - type: recall_at_3
      value: 38.731
    - type: recall_at_5
      value: 44.433
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 26.510999999999996
    - type: map_at_10
      value: 35.755333333333326
    - type: map_at_100
      value: 36.97525
    - type: map_at_1000
      value: 37.08741666666667
    - type: map_at_3
      value: 32.921
    - type: map_at_5
      value: 34.45041666666667
    - type: mrr_at_1
      value: 31.578416666666666
    - type: mrr_at_10
      value: 40.06066666666667
    - type: mrr_at_100
      value: 40.93350000000001
    - type: mrr_at_1000
      value: 40.98716666666667
    - type: mrr_at_3
      value: 37.710499999999996
    - type: mrr_at_5
      value: 39.033249999999995
    - type: ndcg_at_1
      value: 31.578416666666666
    - type: ndcg_at_10
      value: 41.138666666666666
    - type: ndcg_at_100
      value: 46.37291666666666
    - type: ndcg_at_1000
      value: 48.587500000000006
    - type: ndcg_at_3
      value: 36.397083333333335
    - type: ndcg_at_5
      value: 38.539
    - type: precision_at_1
      value: 31.578416666666666
    - type: precision_at_10
      value: 7.221583333333332
    - type: precision_at_100
      value: 1.1581666666666668
    - type: precision_at_1000
      value: 0.15416666666666667
    - type: precision_at_3
      value: 16.758
    - type: precision_at_5
      value: 11.830916666666665
    - type: recall_at_1
      value: 26.510999999999996
    - type: recall_at_10
      value: 52.7825
    - type: recall_at_100
      value: 75.79675
    - type: recall_at_1000
      value: 91.10483333333335
    - type: recall_at_3
      value: 39.48233333333334
    - type: recall_at_5
      value: 45.07116666666667
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 24.564
    - type: map_at_10
      value: 31.235000000000003
    - type: map_at_100
      value: 32.124
    - type: map_at_1000
      value: 32.216
    - type: map_at_3
      value: 29.330000000000002
    - type: map_at_5
      value: 30.379
    - type: mrr_at_1
      value: 27.761000000000003
    - type: mrr_at_10
      value: 34.093
    - type: mrr_at_100
      value: 34.885
    - type: mrr_at_1000
      value: 34.957
    - type: mrr_at_3
      value: 32.388
    - type: mrr_at_5
      value: 33.269
    - type: ndcg_at_1
      value: 27.761000000000003
    - type: ndcg_at_10
      value: 35.146
    - type: ndcg_at_100
      value: 39.597
    - type: ndcg_at_1000
      value: 42.163000000000004
    - type: ndcg_at_3
      value: 31.674000000000003
    - type: ndcg_at_5
      value: 33.224
    - type: precision_at_1
      value: 27.761000000000003
    - type: precision_at_10
      value: 5.383
    - type: precision_at_100
      value: 0.836
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 13.599
    - type: precision_at_5
      value: 9.202
    - type: recall_at_1
      value: 24.564
    - type: recall_at_10
      value: 44.36
    - type: recall_at_100
      value: 64.408
    - type: recall_at_1000
      value: 83.892
    - type: recall_at_3
      value: 34.653
    - type: recall_at_5
      value: 38.589
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 17.01
    - type: map_at_10
      value: 24.485
    - type: map_at_100
      value: 25.573
    - type: map_at_1000
      value: 25.703
    - type: map_at_3
      value: 21.953
    - type: map_at_5
      value: 23.294999999999998
    - type: mrr_at_1
      value: 20.544
    - type: mrr_at_10
      value: 28.238000000000003
    - type: mrr_at_100
      value: 29.142000000000003
    - type: mrr_at_1000
      value: 29.219
    - type: mrr_at_3
      value: 25.802999999999997
    - type: mrr_at_5
      value: 27.105
    - type: ndcg_at_1
      value: 20.544
    - type: ndcg_at_10
      value: 29.387999999999998
    - type: ndcg_at_100
      value: 34.603
    - type: ndcg_at_1000
      value: 37.564
    - type: ndcg_at_3
      value: 24.731
    - type: ndcg_at_5
      value: 26.773000000000003
    - type: precision_at_1
      value: 20.544
    - type: precision_at_10
      value: 5.509
    - type: precision_at_100
      value: 0.9450000000000001
    - type: precision_at_1000
      value: 0.13799999999999998
    - type: precision_at_3
      value: 11.757
    - type: precision_at_5
      value: 8.596
    - type: recall_at_1
      value: 17.01
    - type: recall_at_10
      value: 40.392
    - type: recall_at_100
      value: 64.043
    - type: recall_at_1000
      value: 85.031
    - type: recall_at_3
      value: 27.293
    - type: recall_at_5
      value: 32.586999999999996
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 27.155
    - type: map_at_10
      value: 35.92
    - type: map_at_100
      value: 37.034
    - type: map_at_1000
      value: 37.139
    - type: map_at_3
      value: 33.263999999999996
    - type: map_at_5
      value: 34.61
    - type: mrr_at_1
      value: 32.183
    - type: mrr_at_10
      value: 40.099000000000004
    - type: mrr_at_100
      value: 41.001
    - type: mrr_at_1000
      value: 41.059
    - type: mrr_at_3
      value: 37.889
    - type: mrr_at_5
      value: 39.007999999999996
    - type: ndcg_at_1
      value: 32.183
    - type: ndcg_at_10
      value: 41.127
    - type: ndcg_at_100
      value: 46.464
    - type: ndcg_at_1000
      value: 48.67
    - type: ndcg_at_3
      value: 36.396
    - type: ndcg_at_5
      value: 38.313
    - type: precision_at_1
      value: 32.183
    - type: precision_at_10
      value: 6.847
    - type: precision_at_100
      value: 1.0739999999999998
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_3
      value: 16.356
    - type: precision_at_5
      value: 11.362
    - type: recall_at_1
      value: 27.155
    - type: recall_at_10
      value: 52.922000000000004
    - type: recall_at_100
      value: 76.39
    - type: recall_at_1000
      value: 91.553
    - type: recall_at_3
      value: 39.745999999999995
    - type: recall_at_5
      value: 44.637
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 25.523
    - type: map_at_10
      value: 34.268
    - type: map_at_100
      value: 35.835
    - type: map_at_1000
      value: 36.046
    - type: map_at_3
      value: 31.662000000000003
    - type: map_at_5
      value: 32.71
    - type: mrr_at_1
      value: 31.028
    - type: mrr_at_10
      value: 38.924
    - type: mrr_at_100
      value: 39.95
    - type: mrr_at_1000
      value: 40.003
    - type: mrr_at_3
      value: 36.594
    - type: mrr_at_5
      value: 37.701
    - type: ndcg_at_1
      value: 31.028
    - type: ndcg_at_10
      value: 39.848
    - type: ndcg_at_100
      value: 45.721000000000004
    - type: ndcg_at_1000
      value: 48.424
    - type: ndcg_at_3
      value: 35.329
    - type: ndcg_at_5
      value: 36.779
    - type: precision_at_1
      value: 31.028
    - type: precision_at_10
      value: 7.51
    - type: precision_at_100
      value: 1.478
    - type: precision_at_1000
      value: 0.24
    - type: precision_at_3
      value: 16.337
    - type: precision_at_5
      value: 11.383000000000001
    - type: recall_at_1
      value: 25.523
    - type: recall_at_10
      value: 50.735
    - type: recall_at_100
      value: 76.593
    - type: recall_at_1000
      value: 93.771
    - type: recall_at_3
      value: 37.574000000000005
    - type: recall_at_5
      value: 41.602
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 20.746000000000002
    - type: map_at_10
      value: 28.557
    - type: map_at_100
      value: 29.575000000000003
    - type: map_at_1000
      value: 29.659000000000002
    - type: map_at_3
      value: 25.753999999999998
    - type: map_at_5
      value: 27.254
    - type: mrr_at_1
      value: 22.736
    - type: mrr_at_10
      value: 30.769000000000002
    - type: mrr_at_100
      value: 31.655
    - type: mrr_at_1000
      value: 31.717000000000002
    - type: mrr_at_3
      value: 28.065
    - type: mrr_at_5
      value: 29.543999999999997
    - type: ndcg_at_1
      value: 22.736
    - type: ndcg_at_10
      value: 33.545
    - type: ndcg_at_100
      value: 38.743
    - type: ndcg_at_1000
      value: 41.002
    - type: ndcg_at_3
      value: 28.021
    - type: ndcg_at_5
      value: 30.586999999999996
    - type: precision_at_1
      value: 22.736
    - type: precision_at_10
      value: 5.416
    - type: precision_at_100
      value: 0.8710000000000001
    - type: precision_at_1000
      value: 0.116
    - type: precision_at_3
      value: 11.953
    - type: precision_at_5
      value: 8.651
    - type: recall_at_1
      value: 20.746000000000002
    - type: recall_at_10
      value: 46.87
    - type: recall_at_100
      value: 71.25200000000001
    - type: recall_at_1000
      value: 88.26
    - type: recall_at_3
      value: 32.029999999999994
    - type: recall_at_5
      value: 38.21
  - task:
      type: Retrieval
    dataset:
      type: climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 12.105
    - type: map_at_10
      value: 20.577
    - type: map_at_100
      value: 22.686999999999998
    - type: map_at_1000
      value: 22.889
    - type: map_at_3
      value: 17.174
    - type: map_at_5
      value: 18.807
    - type: mrr_at_1
      value: 27.101
    - type: mrr_at_10
      value: 38.475
    - type: mrr_at_100
      value: 39.491
    - type: mrr_at_1000
      value: 39.525
    - type: mrr_at_3
      value: 34.886
    - type: mrr_at_5
      value: 36.922
    - type: ndcg_at_1
      value: 27.101
    - type: ndcg_at_10
      value: 29.002
    - type: ndcg_at_100
      value: 37.218
    - type: ndcg_at_1000
      value: 40.644000000000005
    - type: ndcg_at_3
      value: 23.464
    - type: ndcg_at_5
      value: 25.262
    - type: precision_at_1
      value: 27.101
    - type: precision_at_10
      value: 9.179
    - type: precision_at_100
      value: 1.806
    - type: precision_at_1000
      value: 0.244
    - type: precision_at_3
      value: 17.394000000000002
    - type: precision_at_5
      value: 13.342
    - type: recall_at_1
      value: 12.105
    - type: recall_at_10
      value: 35.143
    - type: recall_at_100
      value: 63.44499999999999
    - type: recall_at_1000
      value: 82.49499999999999
    - type: recall_at_3
      value: 21.489
    - type: recall_at_5
      value: 26.82
  - task:
      type: Retrieval
    dataset:
      type: dbpedia-entity
      name: MTEB DBPedia
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 8.769
    - type: map_at_10
      value: 18.619
    - type: map_at_100
      value: 26.3
    - type: map_at_1000
      value: 28.063
    - type: map_at_3
      value: 13.746
    - type: map_at_5
      value: 16.035
    - type: mrr_at_1
      value: 65.25
    - type: mrr_at_10
      value: 73.678
    - type: mrr_at_100
      value: 73.993
    - type: mrr_at_1000
      value: 74.003
    - type: mrr_at_3
      value: 72.042
    - type: mrr_at_5
      value: 72.992
    - type: ndcg_at_1
      value: 53.625
    - type: ndcg_at_10
      value: 39.638
    - type: ndcg_at_100
      value: 44.601
    - type: ndcg_at_1000
      value: 52.80200000000001
    - type: ndcg_at_3
      value: 44.727
    - type: ndcg_at_5
      value: 42.199
    - type: precision_at_1
      value: 65.25
    - type: precision_at_10
      value: 31.025000000000002
    - type: precision_at_100
      value: 10.174999999999999
    - type: precision_at_1000
      value: 2.0740000000000003
    - type: precision_at_3
      value: 48.083
    - type: precision_at_5
      value: 40.6
    - type: recall_at_1
      value: 8.769
    - type: recall_at_10
      value: 23.910999999999998
    - type: recall_at_100
      value: 51.202999999999996
    - type: recall_at_1000
      value: 77.031
    - type: recall_at_3
      value: 15.387999999999998
    - type: recall_at_5
      value: 18.919
  - task:
      type: Classification
    dataset:
      type: mteb/emotion
      name: MTEB EmotionClassification
      config: default
      split: test
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
    metrics:
    - type: accuracy
      value: 54.47
    - type: f1
      value: 48.21839043361556
  - task:
      type: Retrieval
    dataset:
      type: fever
      name: MTEB FEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 63.564
    - type: map_at_10
      value: 74.236
    - type: map_at_100
      value: 74.53699999999999
    - type: map_at_1000
      value: 74.557
    - type: map_at_3
      value: 72.556
    - type: map_at_5
      value: 73.656
    - type: mrr_at_1
      value: 68.497
    - type: mrr_at_10
      value: 78.373
    - type: mrr_at_100
      value: 78.54299999999999
    - type: mrr_at_1000
      value: 78.549
    - type: mrr_at_3
      value: 77.03
    - type: mrr_at_5
      value: 77.938
    - type: ndcg_at_1
      value: 68.497
    - type: ndcg_at_10
      value: 79.12599999999999
    - type: ndcg_at_100
      value: 80.319
    - type: ndcg_at_1000
      value: 80.71199999999999
    - type: ndcg_at_3
      value: 76.209
    - type: ndcg_at_5
      value: 77.90700000000001
    - type: precision_at_1
      value: 68.497
    - type: precision_at_10
      value: 9.958
    - type: precision_at_100
      value: 1.077
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 29.908
    - type: precision_at_5
      value: 18.971
    - type: recall_at_1
      value: 63.564
    - type: recall_at_10
      value: 90.05199999999999
    - type: recall_at_100
      value: 95.028
    - type: recall_at_1000
      value: 97.667
    - type: recall_at_3
      value: 82.17999999999999
    - type: recall_at_5
      value: 86.388
  - task:
      type: Retrieval
    dataset:
      type: fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 19.042
    - type: map_at_10
      value: 30.764999999999997
    - type: map_at_100
      value: 32.678000000000004
    - type: map_at_1000
      value: 32.881
    - type: map_at_3
      value: 26.525
    - type: map_at_5
      value: 28.932000000000002
    - type: mrr_at_1
      value: 37.653999999999996
    - type: mrr_at_10
      value: 46.597
    - type: mrr_at_100
      value: 47.413
    - type: mrr_at_1000
      value: 47.453
    - type: mrr_at_3
      value: 43.775999999999996
    - type: mrr_at_5
      value: 45.489000000000004
    - type: ndcg_at_1
      value: 37.653999999999996
    - type: ndcg_at_10
      value: 38.615
    - type: ndcg_at_100
      value: 45.513999999999996
    - type: ndcg_at_1000
      value: 48.815999999999995
    - type: ndcg_at_3
      value: 34.427
    - type: ndcg_at_5
      value: 35.954
    - type: precision_at_1
      value: 37.653999999999996
    - type: precision_at_10
      value: 10.864
    - type: precision_at_100
      value: 1.7850000000000001
    - type: precision_at_1000
      value: 0.23800000000000002
    - type: precision_at_3
      value: 22.788
    - type: precision_at_5
      value: 17.346
    - type: recall_at_1
      value: 19.042
    - type: recall_at_10
      value: 45.707
    - type: recall_at_100
      value: 71.152
    - type: recall_at_1000
      value: 90.7
    - type: recall_at_3
      value: 30.814000000000004
    - type: recall_at_5
      value: 37.478
  - task:
      type: Retrieval
    dataset:
      type: hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 38.001000000000005
    - type: map_at_10
      value: 59.611000000000004
    - type: map_at_100
      value: 60.582
    - type: map_at_1000
      value: 60.646
    - type: map_at_3
      value: 56.031
    - type: map_at_5
      value: 58.243
    - type: mrr_at_1
      value: 76.003
    - type: mrr_at_10
      value: 82.15400000000001
    - type: mrr_at_100
      value: 82.377
    - type: mrr_at_1000
      value: 82.383
    - type: mrr_at_3
      value: 81.092
    - type: mrr_at_5
      value: 81.742
    - type: ndcg_at_1
      value: 76.003
    - type: ndcg_at_10
      value: 68.216
    - type: ndcg_at_100
      value: 71.601
    - type: ndcg_at_1000
      value: 72.821
    - type: ndcg_at_3
      value: 63.109
    - type: ndcg_at_5
      value: 65.902
    - type: precision_at_1
      value: 76.003
    - type: precision_at_10
      value: 14.379
    - type: precision_at_100
      value: 1.702
    - type: precision_at_1000
      value: 0.186
    - type: precision_at_3
      value: 40.396
    - type: precision_at_5
      value: 26.442
    - type: recall_at_1
      value: 38.001000000000005
    - type: recall_at_10
      value: 71.897
    - type: recall_at_100
      value: 85.105
    - type: recall_at_1000
      value: 93.133
    - type: recall_at_3
      value: 60.594
    - type: recall_at_5
      value: 66.104
  - task:
      type: Classification
    dataset:
      type: mteb/imdb
      name: MTEB ImdbClassification
      config: default
      split: test
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
    metrics:
    - type: accuracy
      value: 91.31280000000001
    - type: ap
      value: 87.53723467501632
    - type: f1
      value: 91.30282906596291
  - task:
      type: Retrieval
    dataset:
      type: msmarco
      name: MTEB MSMARCO
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 21.917
    - type: map_at_10
      value: 34.117999999999995
    - type: map_at_100
      value: 35.283
    - type: map_at_1000
      value: 35.333999999999996
    - type: map_at_3
      value: 30.330000000000002
    - type: map_at_5
      value: 32.461
    - type: mrr_at_1
      value: 22.579
    - type: mrr_at_10
      value: 34.794000000000004
    - type: mrr_at_100
      value: 35.893
    - type: mrr_at_1000
      value: 35.937000000000005
    - type: mrr_at_3
      value: 31.091
    - type: mrr_at_5
      value: 33.173
    - type: ndcg_at_1
      value: 22.579
    - type: ndcg_at_10
      value: 40.951
    - type: ndcg_at_100
      value: 46.558
    - type: ndcg_at_1000
      value: 47.803000000000004
    - type: ndcg_at_3
      value: 33.262
    - type: ndcg_at_5
      value: 37.036
    - type: precision_at_1
      value: 22.579
    - type: precision_at_10
      value: 6.463000000000001
    - type: precision_at_100
      value: 0.928
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 14.174000000000001
    - type: precision_at_5
      value: 10.421
    - type: recall_at_1
      value: 21.917
    - type: recall_at_10
      value: 61.885
    - type: recall_at_100
      value: 87.847
    - type: recall_at_1000
      value: 97.322
    - type: recall_at_3
      value: 41.010000000000005
    - type: recall_at_5
      value: 50.031000000000006
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (en)
      config: en
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 93.49521203830369
    - type: f1
      value: 93.30882341740241
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (en)
      config: en
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 71.0579115367077
    - type: f1
      value: 51.2368258319339
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (en)
      config: en
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 73.88029589778077
    - type: f1
      value: 72.34422048584663
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (en)
      config: en
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 78.2817753866846
    - type: f1
      value: 77.87746050004304
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-p2p
      name: MTEB MedrxivClusteringP2P
      config: default
      split: test
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
    metrics:
    - type: v_measure
      value: 33.247341454119216
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-s2s
      name: MTEB MedrxivClusteringS2S
      config: default
      split: test
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
    metrics:
    - type: v_measure
      value: 31.9647477166234
  - task:
      type: Reranking
    dataset:
      type: mteb/mind_small
      name: MTEB MindSmallReranking
      config: default
      split: test
      revision: 3bdac13927fdc888b903db93b2ffdbd90b295a69
    metrics:
    - type: map
      value: 31.90698374676892
    - type: mrr
      value: 33.07523683771251
  - task:
      type: Retrieval
    dataset:
      type: nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 6.717
    - type: map_at_10
      value: 14.566
    - type: map_at_100
      value: 18.465999999999998
    - type: map_at_1000
      value: 20.033
    - type: map_at_3
      value: 10.863
    - type: map_at_5
      value: 12.589
    - type: mrr_at_1
      value: 49.845
    - type: mrr_at_10
      value: 58.385
    - type: mrr_at_100
      value: 58.989999999999995
    - type: mrr_at_1000
      value: 59.028999999999996
    - type: mrr_at_3
      value: 56.76
    - type: mrr_at_5
      value: 57.766
    - type: ndcg_at_1
      value: 47.678
    - type: ndcg_at_10
      value: 37.511
    - type: ndcg_at_100
      value: 34.537
    - type: ndcg_at_1000
      value: 43.612
    - type: ndcg_at_3
      value: 43.713
    - type: ndcg_at_5
      value: 41.303
    - type: precision_at_1
      value: 49.845
    - type: precision_at_10
      value: 27.307
    - type: precision_at_100
      value: 8.746
    - type: precision_at_1000
      value: 2.182
    - type: precision_at_3
      value: 40.764
    - type: precision_at_5
      value: 35.232
    - type: recall_at_1
      value: 6.717
    - type: recall_at_10
      value: 18.107
    - type: recall_at_100
      value: 33.759
    - type: recall_at_1000
      value: 67.31
    - type: recall_at_3
      value: 11.68
    - type: recall_at_5
      value: 14.557999999999998
  - task:
      type: Retrieval
    dataset:
      type: nq
      name: MTEB NQ
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 27.633999999999997
    - type: map_at_10
      value: 42.400999999999996
    - type: map_at_100
      value: 43.561
    - type: map_at_1000
      value: 43.592
    - type: map_at_3
      value: 37.865
    - type: map_at_5
      value: 40.650999999999996
    - type: mrr_at_1
      value: 31.286
    - type: mrr_at_10
      value: 44.996
    - type: mrr_at_100
      value: 45.889
    - type: mrr_at_1000
      value: 45.911
    - type: mrr_at_3
      value: 41.126000000000005
    - type: mrr_at_5
      value: 43.536
    - type: ndcg_at_1
      value: 31.257
    - type: ndcg_at_10
      value: 50.197
    - type: ndcg_at_100
      value: 55.062
    - type: ndcg_at_1000
      value: 55.81700000000001
    - type: ndcg_at_3
      value: 41.650999999999996
    - type: ndcg_at_5
      value: 46.324
    - type: precision_at_1
      value: 31.257
    - type: precision_at_10
      value: 8.508000000000001
    - type: precision_at_100
      value: 1.121
    - type: precision_at_1000
      value: 0.11900000000000001
    - type: precision_at_3
      value: 19.1
    - type: precision_at_5
      value: 14.16
    - type: recall_at_1
      value: 27.633999999999997
    - type: recall_at_10
      value: 71.40100000000001
    - type: recall_at_100
      value: 92.463
    - type: recall_at_1000
      value: 98.13199999999999
    - type: recall_at_3
      value: 49.382
    - type: recall_at_5
      value: 60.144
  - task:
      type: Retrieval
    dataset:
      type: quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 71.17099999999999
    - type: map_at_10
      value: 85.036
    - type: map_at_100
      value: 85.67099999999999
    - type: map_at_1000
      value: 85.68599999999999
    - type: map_at_3
      value: 82.086
    - type: map_at_5
      value: 83.956
    - type: mrr_at_1
      value: 82.04
    - type: mrr_at_10
      value: 88.018
    - type: mrr_at_100
      value: 88.114
    - type: mrr_at_1000
      value: 88.115
    - type: mrr_at_3
      value: 87.047
    - type: mrr_at_5
      value: 87.73100000000001
    - type: ndcg_at_1
      value: 82.03
    - type: ndcg_at_10
      value: 88.717
    - type: ndcg_at_100
      value: 89.904
    - type: ndcg_at_1000
      value: 89.991
    - type: ndcg_at_3
      value: 85.89099999999999
    - type: ndcg_at_5
      value: 87.485
    - type: precision_at_1
      value: 82.03
    - type: precision_at_10
      value: 13.444999999999999
    - type: precision_at_100
      value: 1.533
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 37.537
    - type: precision_at_5
      value: 24.692
    - type: recall_at_1
      value: 71.17099999999999
    - type: recall_at_10
      value: 95.634
    - type: recall_at_100
      value: 99.614
    - type: recall_at_1000
      value: 99.99
    - type: recall_at_3
      value: 87.48
    - type: recall_at_5
      value: 91.996
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering
      name: MTEB RedditClustering
      config: default
      split: test
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
    metrics:
    - type: v_measure
      value: 55.067219624685315
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering-p2p
      name: MTEB RedditClusteringP2P
      config: default
      split: test
      revision: 282350215ef01743dc01b456c7f5241fa8937f16
    metrics:
    - type: v_measure
      value: 62.121822992300444
  - task:
      type: Retrieval
    dataset:
      type: scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 4.153
    - type: map_at_10
      value: 11.024000000000001
    - type: map_at_100
      value: 13.233
    - type: map_at_1000
      value: 13.62
    - type: map_at_3
      value: 7.779999999999999
    - type: map_at_5
      value: 9.529
    - type: mrr_at_1
      value: 20.599999999999998
    - type: mrr_at_10
      value: 31.361
    - type: mrr_at_100
      value: 32.738
    - type: mrr_at_1000
      value: 32.792
    - type: mrr_at_3
      value: 28.15
    - type: mrr_at_5
      value: 30.085
    - type: ndcg_at_1
      value: 20.599999999999998
    - type: ndcg_at_10
      value: 18.583
    - type: ndcg_at_100
      value: 27.590999999999998
    - type: ndcg_at_1000
      value: 34.001
    - type: ndcg_at_3
      value: 17.455000000000002
    - type: ndcg_at_5
      value: 15.588
    - type: precision_at_1
      value: 20.599999999999998
    - type: precision_at_10
      value: 9.74
    - type: precision_at_100
      value: 2.284
    - type: precision_at_1000
      value: 0.381
    - type: precision_at_3
      value: 16.533
    - type: precision_at_5
      value: 14.02
    - type: recall_at_1
      value: 4.153
    - type: recall_at_10
      value: 19.738
    - type: recall_at_100
      value: 46.322
    - type: recall_at_1000
      value: 77.378
    - type: recall_at_3
      value: 10.048
    - type: recall_at_5
      value: 14.233
  - task:
      type: STS
    dataset:
      type: mteb/sickr-sts
      name: MTEB SICK-R
      config: default
      split: test
      revision: a6ea5a8cab320b040a23452cc28066d9beae2cee
    metrics:
    - type: cos_sim_pearson
      value: 85.07097501003639
    - type: cos_sim_spearman
      value: 81.05827848407056
    - type: euclidean_pearson
      value: 82.6279003372546
    - type: euclidean_spearman
      value: 81.00031515279802
    - type: manhattan_pearson
      value: 82.59338284959495
    - type: manhattan_spearman
      value: 80.97432711064945
  - task:
      type: STS
    dataset:
      type: mteb/sts12-sts
      name: MTEB STS12
      config: default
      split: test
      revision: a0d554a64d88156834ff5ae9920b964011b16384
    metrics:
    - type: cos_sim_pearson
      value: 86.28991993621685
    - type: cos_sim_spearman
      value: 78.71828082424351
    - type: euclidean_pearson
      value: 83.4881331520832
    - type: euclidean_spearman
      value: 78.51746826842316
    - type: manhattan_pearson
      value: 83.4109223774324
    - type: manhattan_spearman
      value: 78.431544382179
  - task:
      type: STS
    dataset:
      type: mteb/sts13-sts
      name: MTEB STS13
      config: default
      split: test
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
    metrics:
    - type: cos_sim_pearson
      value: 83.16651661072123
    - type: cos_sim_spearman
      value: 84.88094386637867
    - type: euclidean_pearson
      value: 84.3547603585416
    - type: euclidean_spearman
      value: 84.85148665860193
    - type: manhattan_pearson
      value: 84.29648369879266
    - type: manhattan_spearman
      value: 84.76074870571124
  - task:
      type: STS
    dataset:
      type: mteb/sts14-sts
      name: MTEB STS14
      config: default
      split: test
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
    metrics:
    - type: cos_sim_pearson
      value: 83.40596254292149
    - type: cos_sim_spearman
      value: 83.10699573133829
    - type: euclidean_pearson
      value: 83.22794776876958
    - type: euclidean_spearman
      value: 83.22583316084712
    - type: manhattan_pearson
      value: 83.15899233935681
    - type: manhattan_spearman
      value: 83.17668293648019
  - task:
      type: STS
    dataset:
      type: mteb/sts15-sts
      name: MTEB STS15
      config: default
      split: test
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
    metrics:
    - type: cos_sim_pearson
      value: 87.27977121352563
    - type: cos_sim_spearman
      value: 88.73903130248591
    - type: euclidean_pearson
      value: 88.30685958438735
    - type: euclidean_spearman
      value: 88.79755484280406
    - type: manhattan_pearson
      value: 88.30305607758652
    - type: manhattan_spearman
      value: 88.80096577072784
  - task:
      type: STS
    dataset:
      type: mteb/sts16-sts
      name: MTEB STS16
      config: default
      split: test
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
    metrics:
    - type: cos_sim_pearson
      value: 84.08819031430218
    - type: cos_sim_spearman
      value: 86.35414445951125
    - type: euclidean_pearson
      value: 85.4683192388315
    - type: euclidean_spearman
      value: 86.2079674669473
    - type: manhattan_pearson
      value: 85.35835702257341
    - type: manhattan_spearman
      value: 86.08483380002187
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-en)
      config: en-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 87.36149449801478
    - type: cos_sim_spearman
      value: 87.7102980757725
    - type: euclidean_pearson
      value: 88.16457177837161
    - type: euclidean_spearman
      value: 87.6598652482716
    - type: manhattan_pearson
      value: 88.23894728971618
    - type: manhattan_spearman
      value: 87.74470156709361
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (en)
      config: en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 64.54023758394433
    - type: cos_sim_spearman
      value: 66.28491960187773
    - type: euclidean_pearson
      value: 67.0853128483472
    - type: euclidean_spearman
      value: 66.10307543766307
    - type: manhattan_pearson
      value: 66.7635365592556
    - type: manhattan_spearman
      value: 65.76408004780167
  - task:
      type: STS
    dataset:
      type: mteb/stsbenchmark-sts
      name: MTEB STSBenchmark
      config: default
      split: test
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
    metrics:
    - type: cos_sim_pearson
      value: 85.15858398195317
    - type: cos_sim_spearman
      value: 87.44850004752102
    - type: euclidean_pearson
      value: 86.60737082550408
    - type: euclidean_spearman
      value: 87.31591549824242
    - type: manhattan_pearson
      value: 86.56187011429977
    - type: manhattan_spearman
      value: 87.23854795795319
  - task:
      type: Reranking
    dataset:
      type: mteb/scidocs-reranking
      name: MTEB SciDocsRR
      config: default
      split: test
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
    metrics:
    - type: map
      value: 86.66210488769109
    - type: mrr
      value: 96.23100664767331
  - task:
      type: Retrieval
    dataset:
      type: scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 56.094
    - type: map_at_10
      value: 67.486
    - type: map_at_100
      value: 67.925
    - type: map_at_1000
      value: 67.949
    - type: map_at_3
      value: 64.857
    - type: map_at_5
      value: 66.31
    - type: mrr_at_1
      value: 58.667
    - type: mrr_at_10
      value: 68.438
    - type: mrr_at_100
      value: 68.733
    - type: mrr_at_1000
      value: 68.757
    - type: mrr_at_3
      value: 66.389
    - type: mrr_at_5
      value: 67.456
    - type: ndcg_at_1
      value: 58.667
    - type: ndcg_at_10
      value: 72.506
    - type: ndcg_at_100
      value: 74.27
    - type: ndcg_at_1000
      value: 74.94800000000001
    - type: ndcg_at_3
      value: 67.977
    - type: ndcg_at_5
      value: 70.028
    - type: precision_at_1
      value: 58.667
    - type: precision_at_10
      value: 9.767000000000001
    - type: precision_at_100
      value: 1.073
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 27.0
    - type: precision_at_5
      value: 17.666999999999998
    - type: recall_at_1
      value: 56.094
    - type: recall_at_10
      value: 86.68900000000001
    - type: recall_at_100
      value: 94.333
    - type: recall_at_1000
      value: 99.667
    - type: recall_at_3
      value: 74.522
    - type: recall_at_5
      value: 79.611
  - task:
      type: PairClassification
    dataset:
      type: mteb/sprintduplicatequestions-pairclassification
      name: MTEB SprintDuplicateQuestions
      config: default
      split: test
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
    metrics:
    - type: cos_sim_accuracy
      value: 99.83069306930693
    - type: cos_sim_ap
      value: 95.69184662911199
    - type: cos_sim_f1
      value: 91.4027149321267
    - type: cos_sim_precision
      value: 91.91102123356926
    - type: cos_sim_recall
      value: 90.9
    - type: dot_accuracy
      value: 99.69405940594059
    - type: dot_ap
      value: 90.21674151456216
    - type: dot_f1
      value: 84.4489179667841
    - type: dot_precision
      value: 85.00506585612969
    - type: dot_recall
      value: 83.89999999999999
    - type: euclidean_accuracy
      value: 99.83069306930693
    - type: euclidean_ap
      value: 95.67760109671087
    - type: euclidean_f1
      value: 91.19754350051177
    - type: euclidean_precision
      value: 93.39622641509435
    - type: euclidean_recall
      value: 89.1
    - type: manhattan_accuracy
      value: 99.83267326732673
    - type: manhattan_ap
      value: 95.69771347732625
    - type: manhattan_f1
      value: 91.32420091324201
    - type: manhattan_precision
      value: 92.68795056642637
    - type: manhattan_recall
      value: 90.0
    - type: max_accuracy
      value: 99.83267326732673
    - type: max_ap
      value: 95.69771347732625
    - type: max_f1
      value: 91.4027149321267
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering
      name: MTEB StackExchangeClustering
      config: default
      split: test
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
    metrics:
    - type: v_measure
      value: 64.47378332953092
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering-p2p
      name: MTEB StackExchangeClusteringP2P
      config: default
      split: test
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
    metrics:
    - type: v_measure
      value: 33.79602531604151
  - task:
      type: Reranking
    dataset:
      type: mteb/stackoverflowdupquestions-reranking
      name: MTEB StackOverflowDupQuestions
      config: default
      split: test
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
    metrics:
    - type: map
      value: 53.80707639107175
    - type: mrr
      value: 54.64886522790935
  - task:
      type: Summarization
    dataset:
      type: mteb/summeval
      name: MTEB SummEval
      config: default
      split: test
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
    metrics:
    - type: cos_sim_pearson
      value: 30.852448373051395
    - type: cos_sim_spearman
      value: 32.51821499493775
    - type: dot_pearson
      value: 30.390650062190456
    - type: dot_spearman
      value: 30.588836159667636
  - task:
      type: Retrieval
    dataset:
      type: trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 0.198
    - type: map_at_10
      value: 1.51
    - type: map_at_100
      value: 8.882
    - type: map_at_1000
      value: 22.181
    - type: map_at_3
      value: 0.553
    - type: map_at_5
      value: 0.843
    - type: mrr_at_1
      value: 74.0
    - type: mrr_at_10
      value: 84.89999999999999
    - type: mrr_at_100
      value: 84.89999999999999
    - type: mrr_at_1000
      value: 84.89999999999999
    - type: mrr_at_3
      value: 84.0
    - type: mrr_at_5
      value: 84.89999999999999
    - type: ndcg_at_1
      value: 68.0
    - type: ndcg_at_10
      value: 64.792
    - type: ndcg_at_100
      value: 51.37199999999999
    - type: ndcg_at_1000
      value: 47.392
    - type: ndcg_at_3
      value: 68.46900000000001
    - type: ndcg_at_5
      value: 67.084
    - type: precision_at_1
      value: 74.0
    - type: precision_at_10
      value: 69.39999999999999
    - type: precision_at_100
      value: 53.080000000000005
    - type: precision_at_1000
      value: 21.258
    - type: precision_at_3
      value: 76.0
    - type: precision_at_5
      value: 73.2
    - type: recall_at_1
      value: 0.198
    - type: recall_at_10
      value: 1.7950000000000002
    - type: recall_at_100
      value: 12.626999999999999
    - type: recall_at_1000
      value: 44.84
    - type: recall_at_3
      value: 0.611
    - type: recall_at_5
      value: 0.959
  - task:
      type: Retrieval
    dataset:
      type: webis-touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 1.4949999999999999
    - type: map_at_10
      value: 8.797
    - type: map_at_100
      value: 14.889
    - type: map_at_1000
      value: 16.309
    - type: map_at_3
      value: 4.389
    - type: map_at_5
      value: 6.776
    - type: mrr_at_1
      value: 18.367
    - type: mrr_at_10
      value: 35.844
    - type: mrr_at_100
      value: 37.119
    - type: mrr_at_1000
      value: 37.119
    - type: mrr_at_3
      value: 30.612000000000002
    - type: mrr_at_5
      value: 33.163
    - type: ndcg_at_1
      value: 16.326999999999998
    - type: ndcg_at_10
      value: 21.9
    - type: ndcg_at_100
      value: 34.705000000000005
    - type: ndcg_at_1000
      value: 45.709
    - type: ndcg_at_3
      value: 22.7
    - type: ndcg_at_5
      value: 23.197000000000003
    - type: precision_at_1
      value: 18.367
    - type: precision_at_10
      value: 21.02
    - type: precision_at_100
      value: 7.714
    - type: precision_at_1000
      value: 1.504
    - type: precision_at_3
      value: 26.531
    - type: precision_at_5
      value: 26.122
    - type: recall_at_1
      value: 1.4949999999999999
    - type: recall_at_10
      value: 15.504000000000001
    - type: recall_at_100
      value: 47.978
    - type: recall_at_1000
      value: 81.56
    - type: recall_at_3
      value: 5.569
    - type: recall_at_5
      value: 9.821
  - task:
      type: Classification
    dataset:
      type: mteb/toxic_conversations_50k
      name: MTEB ToxicConversationsClassification
      config: default
      split: test
      revision: d7c0de2777da35d6aae2200a62c6e0e5af397c4c
    metrics:
    - type: accuracy
      value: 72.99279999999999
    - type: ap
      value: 15.459189680101492
    - type: f1
      value: 56.33023271441895
  - task:
      type: Classification
    dataset:
      type: mteb/tweet_sentiment_extraction
      name: MTEB TweetSentimentExtractionClassification
      config: default
      split: test
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
    metrics:
    - type: accuracy
      value: 63.070175438596486
    - type: f1
      value: 63.28070758709465
  - task:
      type: Clustering
    dataset:
      type: mteb/twentynewsgroups-clustering
      name: MTEB TwentyNewsgroupsClustering
      config: default
      split: test
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
    metrics:
    - type: v_measure
      value: 50.076231309703054
  - task:
      type: PairClassification
    dataset:
      type: mteb/twittersemeval2015-pairclassification
      name: MTEB TwitterSemEval2015
      config: default
      split: test
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
    metrics:
    - type: cos_sim_accuracy
      value: 87.21463908922931
    - type: cos_sim_ap
      value: 77.67287017966282
    - type: cos_sim_f1
      value: 70.34412955465588
    - type: cos_sim_precision
      value: 67.57413709285368
    - type: cos_sim_recall
      value: 73.35092348284961
    - type: dot_accuracy
      value: 85.04500208618943
    - type: dot_ap
      value: 70.4075203869744
    - type: dot_f1
      value: 66.18172537008678
    - type: dot_precision
      value: 64.08798813643104
    - type: dot_recall
      value: 68.41688654353561
    - type: euclidean_accuracy
      value: 87.17887584192646
    - type: euclidean_ap
      value: 77.5774128274464
    - type: euclidean_f1
      value: 70.09307972480777
    - type: euclidean_precision
      value: 71.70852884349986
    - type: euclidean_recall
      value: 68.54881266490766
    - type: manhattan_accuracy
      value: 87.28020504261787
    - type: manhattan_ap
      value: 77.57835820297892
    - type: manhattan_f1
      value: 70.23063591521131
    - type: manhattan_precision
      value: 70.97817299919159
    - type: manhattan_recall
      value: 69.49868073878628
    - type: max_accuracy
      value: 87.28020504261787
    - type: max_ap
      value: 77.67287017966282
    - type: max_f1
      value: 70.34412955465588
  - task:
      type: PairClassification
    dataset:
      type: mteb/twitterurlcorpus-pairclassification
      name: MTEB TwitterURLCorpus
      config: default
      split: test
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
    metrics:
    - type: cos_sim_accuracy
      value: 88.96650754841464
    - type: cos_sim_ap
      value: 86.00185968965064
    - type: cos_sim_f1
      value: 77.95861256351718
    - type: cos_sim_precision
      value: 74.70712773465067
    - type: cos_sim_recall
      value: 81.50600554357868
    - type: dot_accuracy
      value: 87.36950362867233
    - type: dot_ap
      value: 82.22071181147555
    - type: dot_f1
      value: 74.85680716698488
    - type: dot_precision
      value: 71.54688377316114
    - type: dot_recall
      value: 78.48783492454572
    - type: euclidean_accuracy
      value: 88.99561454573679
    - type: euclidean_ap
      value: 86.15882097229648
    - type: euclidean_f1
      value: 78.18463125322332
    - type: euclidean_precision
      value: 74.95408956067241
    - type: euclidean_recall
      value: 81.70619032953496
    - type: manhattan_accuracy
      value: 88.96650754841464
    - type: manhattan_ap
      value: 86.13133111232099
    - type: manhattan_f1
      value: 78.10771470160115
    - type: manhattan_precision
      value: 74.05465084184377
    - type: manhattan_recall
      value: 82.63012011087157
    - type: max_accuracy
      value: 88.99561454573679
    - type: max_ap
      value: 86.15882097229648
    - type: max_f1
      value: 78.18463125322332
language:
- en
license: mit
---

## stella model

**新闻 | News**

**[2023-10-19]** 开源stella-base-en-v2 使用简单，**不需要任何前缀文本**。
Release stella-base-en-v2. This model **does not need any prefix text**.\
**[2023-10-12]** 开源stella-base-zh-v2和stella-large-zh-v2, 效果更好且使用简单，**不需要任何前缀文本**。
Release stella-base-zh-v2 and stella-large-zh-v2. The 2 models have better performance
and **do not need any prefix text**.\
**[2023-09-11]** 开源stella-base-zh和stella-large-zh

stella是一个通用的文本编码模型，主要有以下模型：

|     Model Name     | Model Size (GB) | Dimension | Sequence Length | Language | Need instruction for retrieval? |
|:------------------:|:---------------:|:---------:|:---------------:|:--------:|:-------------------------------:|
| stella-base-en-v2  |       0.2       |    768    |       512       | English  |               No                |
| stella-large-zh-v2 |      0.65       |   1024    |      1024       | Chinese  |               No                |
| stella-base-zh-v2  |       0.2       |    768    |      1024       | Chinese  |               No                |
|  stella-large-zh   |      0.65       |   1024    |      1024       | Chinese  |               Yes               |
|   stella-base-zh   |       0.2       |    768    |      1024       | Chinese  |               Yes               |

完整的训练思路和训练过程已记录在[博客1](https://zhuanlan.zhihu.com/p/655322183)和[博客2](https://zhuanlan.zhihu.com/p/662209559)，欢迎阅读讨论。

**训练数据：**

1. 开源数据(wudao_base_200GB[1]、m3e[2]和simclue[3])，着重挑选了长度大于512的文本
2. 在通用语料库上使用LLM构造一批(question, paragraph)和(sentence, paragraph)数据

**训练方法：**

1. 对比学习损失函数
2. 带有难负例的对比学习损失函数(分别基于bm25和vector构造了难负例)
3. EWC(Elastic Weights Consolidation)[4]
4. cosent loss[5]
5. 每一种类型的数据一个迭代器，分别计算loss进行更新

stella-v2在stella模型的基础上，使用了更多的训练数据，同时知识蒸馏等方法去除了前置的instruction(
比如piccolo的`查询:`, `结果:`, e5的`query:`和`passage:`)。

**初始权重：**\
stella-base-zh和stella-large-zh分别以piccolo-base-zh[6]和piccolo-large-zh作为基础模型，512-1024的position
embedding使用层次分解位置编码[7]进行初始化。\
感谢商汤科技研究院开源的[piccolo系列模型](https://huggingface.co/sensenova)。

stella is a general-purpose text encoder, which mainly includes the following models:

|     Model Name     | Model Size (GB) | Dimension | Sequence Length | Language | Need instruction for retrieval? |
|:------------------:|:---------------:|:---------:|:---------------:|:--------:|:-------------------------------:|
| stella-base-en-v2  |       0.2       |    768    |       512       | English  |               No                |
| stella-large-zh-v2 |      0.65       |   1024    |      1024       | Chinese  |               No                |
| stella-base-zh-v2  |       0.2       |    768    |      1024       | Chinese  |               No                |
|  stella-large-zh   |      0.65       |   1024    |      1024       | Chinese  |               Yes               |
|   stella-base-zh   |       0.2       |    768    |      1024       | Chinese  |               Yes               |

The training data mainly includes:

1. Open-source training data (wudao_base_200GB, m3e, and simclue), with a focus on selecting texts with lengths greater
   than 512.
2. A batch of (question, paragraph) and (sentence, paragraph) data constructed on a general corpus using LLM.

The loss functions mainly include:

1. Contrastive learning loss function
2. Contrastive learning loss function with hard negative examples (based on bm25 and vector hard negatives)
3. EWC (Elastic Weights Consolidation)
4. cosent loss

Model weight initialization:\
stella-base-zh and stella-large-zh use piccolo-base-zh and piccolo-large-zh as the base models, respectively, and the
512-1024 position embedding uses the initialization strategy of hierarchical decomposed position encoding.

Training strategy:\
One iterator for each type of data, separately calculating the loss.

Based on stella models, stella-v2 use more training data and remove instruction by Knowledge Distillation.

## Metric

#### C-MTEB leaderboard (Chinese)

|     Model Name     | Model Size (GB) | Dimension | Sequence Length | Average (35) | Classification (9) | Clustering (4) | Pair Classification (2) | Reranking (4) | Retrieval (8) | STS (8) |
|:------------------:|:---------------:|:---------:|:---------------:|:------------:|:------------------:|:--------------:|:-----------------------:|:-------------:|:-------------:|:-------:|
| stella-large-zh-v2 |      0.65       |   1024    |      1024       |    65.13     |       69.05        |     49.16      |          82.68          |     66.41     |     70.14     |  58.66  |
| stella-base-zh-v2  |       0.2       |    768    |      1024       |    64.36     |       68.29        |      49.4      |          79.95          |     66.1      |     70.08     |  56.92  |
|  stella-large-zh   |      0.65       |   1024    |      1024       |    64.54     |       67.62        |     48.65      |          78.72          |     65.98     |     71.02     |  58.3   |
|   stella-base-zh   |       0.2       |    768    |      1024       |    64.16     |       67.77        |      48.7      |          76.09          |     66.95     |     71.07     |  56.54  |

#### MTEB leaderboard (English)

|    Model Name     | Model Size (GB) | Dimension | Sequence Length | Average (56) | Classification (12) | Clustering (11) | Pair Classification (3) | Reranking (4) | Retrieval (15) | STS (10) | Summarization  (1) |
|:-----------------:|:---------------:|:---------:|:---------------:|:------------:|:-------------------:|:---------------:|:-----------------------:|:-------------:|:--------------:|:--------:|:------------------:|
| stella-base-en-v2 |       0.2       |    768    |       512       |    62.61     |        75.28        |      44.9       |          86.45          |     58.77     |      50.1      |  83.02   |       32.52        |

#### Reproduce our results

**C-MTEB:** 

```python
import torch
import numpy as np
from typing import List
from mteb import MTEB
from sentence_transformers import SentenceTransformer


class FastTextEncoder():
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name).cuda().half().eval()
        self.model.max_seq_length = 512

    def encode(
            self,
            input_texts: List[str],
            *args,
            **kwargs
    ):
        new_sens = list(set(input_texts))
        new_sens.sort(key=lambda x: len(x), reverse=True)
        vecs = self.model.encode(
            new_sens, normalize_embeddings=True, convert_to_numpy=True, batch_size=256
        ).astype(np.float32)
        sen2arrid = {sen: idx for idx, sen in enumerate(new_sens)}
        vecs = vecs[[sen2arrid[sen] for sen in input_texts]]
        torch.cuda.empty_cache()
        return vecs


if __name__ == '__main__':
    model_name = "infgrad/stella-base-zh-v2"
    output_folder = "zh_mteb_results/stella-base-zh-v2"
    task_names = [t.description["name"] for t in MTEB(task_langs=['zh', 'zh-CN']).tasks]
    model = FastTextEncoder(model_name)
    for task in task_names:
        MTEB(tasks=[task], task_langs=['zh', 'zh-CN']).run(model, output_folder=output_folder)

```

**MTEB:**

You can use official script to reproduce our result. [scripts/run_mteb_english.py](https://github.com/embeddings-benchmark/mteb/blob/main/scripts/run_mteb_english.py)

#### Evaluation for long text

经过实际观察发现，C-MTEB的评测数据长度基本都是小于512的，
更致命的是那些长度大于512的文本，其重点都在前半部分
这里以CMRC2018的数据为例说明这个问题：

```
question: 《无双大蛇z》是谁旗下ω-force开发的动作游戏？

passage：《无双大蛇z》是光荣旗下ω-force开发的动作游戏，于2009年3月12日登陆索尼playstation3，并于2009年11月27日推......
```

passage长度为800多，大于512，但是对于这个question而言只需要前面40个字就足以检索，多的内容对于模型而言是一种噪声，反而降低了效果。\
简言之，现有数据集的2个问题：\
1）长度大于512的过少\
2）即便大于512，对于检索而言也只需要前512的文本内容\
导致**无法准确评估模型的长文本编码能力。**

为了解决这个问题，搜集了相关开源数据并使用规则进行过滤，最终整理了6份长文本测试集,他们分别是：

- CMRC2018，通用百科
- CAIL，法律阅读理解
- DRCD，繁体百科，已转简体
- Military，军工问答
- Squad，英文阅读理解，已转中文
- Multifieldqa_zh，清华的大模型长文本理解能力评测数据[9]

处理规则是选取答案在512长度之后的文本，短的测试数据会欠采样一下，长短文本占比约为1:2，所以模型既得理解短文本也得理解长文本。
除了Military数据集，我们提供了其他5个测试数据的下载地址：https://drive.google.com/file/d/1WC6EWaCbVgz-vPMDFH4TwAMkLyh5WNcN/view?usp=sharing

评测指标为Recall@5, 结果如下：

|     Dataset     | piccolo-base-zh | piccolo-large-zh | bge-base-zh | bge-large-zh | stella-base-zh | stella-large-zh | 
|:---------------:|:---------------:|:----------------:|:-----------:|:------------:|:--------------:|:---------------:|
|    CMRC2018     |      94.34      |      93.82       |    91.56    |    93.12     |     96.08      |      95.56      | 
|      CAIL       |      28.04      |      33.64       |    31.22    |    33.94     |     34.62      |      37.18      | 
|      DRCD       |      78.25      |       77.9       |    78.34    |    80.26     |     86.14      |      84.58      | 
|    Military     |      76.61      |      73.06       |    75.65    |    75.81     |     83.71      |      80.48      | 
|      Squad      |      91.21      |      86.61       |    87.87    |    90.38     |     93.31      |      91.21      | 
| Multifieldqa_zh |      81.41      |      83.92       |    83.92    |    83.42     |      79.9      |      80.4       | 
|   **Average**   |      74.98      |      74.83       |    74.76    |    76.15     |   **78.96**    |    **78.24**    | 

**注意：** 因为长文本评测数据数量稀少，所以构造时也使用了train部分，如果自行评测，请注意模型的训练数据以免数据泄露。

## Usage

#### stella 中文系列模型

stella-base-zh 和 stella-large-zh: 本模型是在piccolo基础上训练的，因此**用法和piccolo完全一致**
，即在检索重排任务上给query和passage加上`查询: `和`结果: `。对于短短匹配不需要做任何操作。

stella-base-zh-v2 和 stella-large-zh-v2: 本模型使用简单，**任何使用场景中都不需要加前缀文本**。

stella中文系列模型均使用mean pooling做为文本向量。

在sentence-transformer库中的使用方法：

```python
from modelscope import snapshot_download
model_dir = snapshot_download("AI-ModelScope/stella-base-zh-v2", revision='master')

# 对于短对短数据集，下面是通用的使用方式
from sentence_transformers import SentenceTransformer

sentences = ["数据1", "数据2"]
model = SentenceTransformer(model_dir)
print(model.max_seq_length)
embeddings_1 = model.encode(sentences, normalize_embeddings=True)
embeddings_2 = model.encode(sentences, normalize_embeddings=True)
similarity = embeddings_1 @ embeddings_2.T
print(similarity)
```

直接使用modelscope库：

```python
from modelscope import AutoModel, AutoTokenizer
from sklearn.preprocessing import normalize

model = AutoModel.from_pretrained('AI-ModelScope/stella-base-zh-v2')
tokenizer = AutoTokenizer.from_pretrained('AI-ModelScope/stella-base-zh-v2')
sentences = ["数据1", "数据ABCDEFGH"]
batch_data = tokenizer(
    sentences,
    padding="longest",
    return_tensors="pt",
    max_length=1024,
    truncation=True,
)
attention_mask = batch_data["attention_mask"]
model_output = model(**batch_data)
last_hidden = model_output.last_hidden_state.masked_fill(~attention_mask[..., None].bool(), 0.0)
vectors = last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]
# vectors = normalize(vectors, norm="l2", axis=1, )
print(vectors.shape)  # 2,768
```

#### stella models for English

**Using Sentence-Transformers:**

```python
from modelscope import snapshot_download
model_dir = snapshot_download("AI-ModelScope/stella-base-en-v2", revision='master')

from sentence_transformers import SentenceTransformer

sentences = ["one car come", "one car go"]
model = SentenceTransformer(model_dir)
print(model.max_seq_length)
embeddings_1 = model.encode(sentences, normalize_embeddings=True)
embeddings_2 = model.encode(sentences, normalize_embeddings=True)
similarity = embeddings_1 @ embeddings_2.T
print(similarity)
```

**Using modelscope:**

```python
from modelscope import AutoModel, AutoTokenizer
from sklearn.preprocessing import normalize

model = AutoModel.from_pretrained("AI-ModelScope/stella-base-en-v2")
tokenizer = AutoTokenizer.from_pretrained("AI-ModelScope/stella-base-en-v2")
sentences = ["one car come", "one car go"]
batch_data = tokenizer(
    sentences,
    padding="longest",
    return_tensors="pt",
    max_length=512,
    truncation=True,
)
attention_mask = batch_data["attention_mask"]
model_output = model(**batch_data)
last_hidden = model_output.last_hidden_state.masked_fill(~attention_mask[..., None].bool(), 0.0)
vectors = last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]
print(vectors.shape)
```

## Training Detail

**硬件：** 单卡A100-80GB

**环境：** torch1.13.*; transformers-trainer + deepspeed + gradient-checkpointing

**学习率：** 1e-6

**batch_size：** base模型为1024，额外增加20%的难负例；large模型为768，额外增加20%的难负例

**数据量：** 第一版模型约100万，其中用LLM构造的数据约有200K. LLM模型大小为13b。v2系列模型到了2000万训练数据。

## ToDoList

**评测的稳定性：**
评测过程中发现Clustering任务会和官方的结果不一致，大约有±0.0x的小差距，原因是聚类代码没有设置random_seed，差距可以忽略不计，不影响评测结论。

**更高质量的长文本训练和测试数据：** 训练数据多是用13b模型构造的，肯定会存在噪声。
测试数据基本都是从mrc数据整理来的，所以问题都是factoid类型，不符合真实分布。

**OOD的性能：** 虽然近期出现了很多向量编码模型，但是对于不是那么通用的domain，这一众模型包括stella、openai和cohere,
它们的效果均比不上BM25。

## Reference

1. https://www.scidb.cn/en/detail?dataSetId=c6a3fe684227415a9db8e21bac4a15ab
2. https://github.com/wangyuxinwhy/uniem
3. https://github.com/CLUEbenchmark/SimCLUE
4. https://arxiv.org/abs/1612.00796
5. https://kexue.fm/archives/8847
6. https://huggingface.co/sensenova/piccolo-base-zh
7. https://kexue.fm/archives/7947
8. https://github.com/FlagOpen/FlagEmbedding
9. https://github.com/THUDM/LongBench


