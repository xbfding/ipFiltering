for line in $(cat ./out/ip_out.txt)
do
	echo "./plug/nali.exe ${line}"
	./plug/nali.exe ${line} >> ./out/nali_out.txt
done
