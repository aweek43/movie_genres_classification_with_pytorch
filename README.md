# movie_genres_classification_with_pytorch

프레임워크는 Pytorch

모델은 DenseNet121 (pretrained=True)

optimizer은 optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)

목적함수는 nn.BCEWithLogitsLoss()

데이터셋은 Kaggle의 영화포스터 데이터셋을 이용했습니다.

배치사이즈는 google colab의 메모리 문제로 32로 설정했습니다.

​

Kaggle의 csv형식의 데이터셋에 포스터의 web url이 있는데 따로 함수를 돌려 해당 url의 사진을

모두 다운로드했습니다. 이 중 깨진 파일이 많아 다시 정상적인 사진만 골라냈습니다.

train : test 데이터셋의 비율은 8:2입니다.

모델 학습에는 google colab에서 GPU를 이용했고 demo는 개인pc CPU를 이용했습니다.

train.py는 cpu용 코드이고 train.ipynb가 google colab에서 돌린 GPU용 학습 코드입니다.

​

영화에 따라 장르가 2~4개로 개수가 다르기 때문에 accruracy는 못구하고 Loss값만 구했습니다.

사진에 label이 없기 때문에 다운로드받을 때 사진 파일이름으로 label을 줬습니다.(총 28개의 장르가 있고

해당 장르일 경우 1, 아닐 경우 0)

따라서 Dataloader에서 해당 파일의 이름을 불러와 string을 모델의 output에 맞게 tensor형으로 바꿔

return해주는 클래스를 만들었습니다.

​

demo 방법은 sample/sample 폴더 안에 포스터 사진(jpg)를 넣은 뒤 demo.py를 실행시키면 됩니다.

torch, torchvision 등의 패키지를 다운받아야 합니다.

​

demo 결과 영화 '마약왕'의 장르는 범죄,드라마 인데 모델은 범죄, 드라마, 스릴러 라고 판별했습니다.(가장 높은 3개의 장르를 판별합니다.)

대부분의 장르에서 높은 정확도를 보이지만 애니메이션의 경우 영화 포스터에 의한 장르..라기보다는 제작 과정인 느낌이라(제 추측입니다) 장르로써 애니메이션이라고 나오는 경우가 드뭅니다.

​

Loss는 8 epoch만에 거의 수렴하는 모습을 보였고 overfitting이 되기 전 20 epoch의 모델을 첨부했습니다.
