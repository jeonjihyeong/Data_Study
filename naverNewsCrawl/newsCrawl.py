def main():
    node = 'news'
    cnt=0
    jsonResult=[]

    jsonResponse=getNaverSearch(node,srcText,1,100)#[CODE2]
    total = jsonResponse['total']

    while((jsonResponse!=None)and (jsonResponse['display']!=0)):
        for post in jsonResponse['items']:
            cnt+=1
            getPostData(post,jsonResult,cnt)#[CODE3]

        start=jsonResponse['start']+jsonResponse['display']
        jsonResponse=getNaverSearch(node, srcText,start,100)#[CODE2]

    print('전체검색: %d 건'%total)

    with open('$s_naver_%s.json'%(srcText,node),'w',encoding='utf8')as outfile:
        jsonFile=json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)

        outfile.write(jsonFile)

    print("가져온데이터: %d 건" %(cnt))
    print("%s_naver_$s.json SAVED"%(srcText, node))
    