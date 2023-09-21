import math
import pefile
from hashlib import md5

api_columns = ['API/DLL_0', 'API/DLL_1', 'API/DLL_2', 'API/DLL_3', 'API/DLL_4', 'API/DLL_5', 'API/DLL_6', 'API/DLL_7', 'API/DLL_8', 'API/DLL_9', 'API/DLL_10', 'API/DLL_11', 'API/DLL_12', 'API/DLL_13', 'API/DLL_14', 'API/DLL_15', 'API/DLL_16', 'API/DLL_17', 'API/DLL_18', 'API/DLL_19', 'API/DLL_20', 'API/DLL_21', 'API/DLL_22', 'API/DLL_23', 'API/DLL_24', 'API/DLL_25', 'API/DLL_26', 'API/DLL_27', 'API/DLL_28', 'API/DLL_29', 'API/DLL_30', 'API/DLL_31', 'API/DLL_32', 'API/DLL_33', 'API/DLL_34', 'API/DLL_35', 'API/DLL_36', 'API/DLL_37', 'API/DLL_38', 'API/DLL_39', 'API/DLL_40', 'API/DLL_41', 'API/DLL_42', 'API/DLL_43', 'API/DLL_44', 'API/DLL_45', 'API/DLL_46', 'API/DLL_47', 'API/DLL_48', 'API/DLL_49', 'API/DLL_50', 'API/DLL_51', 'API/DLL_52', 'API/DLL_53', 'API/DLL_54', 'API/DLL_55', 'API/DLL_56', 'API/DLL_57', 'API/DLL_58', 'API/DLL_59', 'API/DLL_60', 'API/DLL_61', 'API/DLL_62', 'API/DLL_63', 'API/DLL_64', 'API/DLL_65', 'API/DLL_66', 'API/DLL_67', 'API/DLL_68', 'API/DLL_69', 'API/DLL_70', 'API/DLL_71', 'API/DLL_72', 'API/DLL_73', 'API/DLL_74', 'API/DLL_75', 'API/DLL_76', 'API/DLL_77', 'API/DLL_78', 'API/DLL_79', 'API/DLL_80', 'API/DLL_81', 'API/DLL_82', 'API/DLL_83', 'API/DLL_84', 'API/DLL_85', 'API/DLL_86', 'API/DLL_87', 'API/DLL_88', 'API/DLL_89', 'API/DLL_90', 'API/DLL_91', 'API/DLL_92', 'API/DLL_93', 'API/DLL_94', 'API/DLL_95', 'API/DLL_96', 'API/DLL_97', 'API/DLL_98', 'API/DLL_99', 'API/DLL_100', 'API/DLL_101', 'API/DLL_102', 'API/DLL_103', 'API/DLL_104', 'API/DLL_105', 'API/DLL_106', 'API/DLL_107', 'API/DLL_108', 'API/DLL_109', 'API/DLL_110', 'API/DLL_111', 'API/DLL_112', 'API/DLL_113', 'API/DLL_114', 'API/DLL_115', 'API/DLL_116', 'API/DLL_117', 'API/DLL_118', 'API/DLL_119', 'API/DLL_120', 'API/DLL_121', 'API/DLL_122', 'API/DLL_123', 'API/DLL_124', 'API/DLL_125', 'API/DLL_126', 'API/DLL_127', 'API/DLL_128', 'API/DLL_129', 'API/DLL_130', 'API/DLL_131', 'API/DLL_132', 'API/DLL_133', 'API/DLL_134', 'API/DLL_135', 'API/DLL_136', 'API/DLL_137', 'API/DLL_138', 'API/DLL_139', 'API/DLL_140', 'API/DLL_141', 'API/DLL_142', 'API/DLL_143', 'API/DLL_144', 'API/DLL_145', 'API/DLL_146', 'API/DLL_147', 'API/DLL_148', 'API/DLL_149', 'API/DLL_150', 'API/DLL_151', 'API/DLL_152', 'API/DLL_153', 'API/DLL_154', 'API/DLL_155', 'API/DLL_156', 'API/DLL_157', 'API/DLL_158', 'API/DLL_159', 'API/DLL_160', 'API/DLL_161', 'API/DLL_162', 'API/DLL_163', 'API/DLL_164', 'API/DLL_165', 'API/DLL_166', 'API/DLL_167', 'API/DLL_168', 'API/DLL_169', 'API/DLL_170', 'API/DLL_171', 'API/DLL_172', 'API/DLL_173', 'API/DLL_174', 'API/DLL_175', 'API/DLL_176', 'API/DLL_177', 'API/DLL_178', 'API/DLL_179', 'API/DLL_180', 'API/DLL_181', 'API/DLL_182', 'API/DLL_183', 'API/DLL_184', 'API/DLL_185', 'API/DLL_186', 'API/DLL_187', 'API/DLL_188', 'API/DLL_189', 'API/DLL_190', 'API/DLL_191', 'API/DLL_192', 'API/DLL_193', 'API/DLL_194', 'API/DLL_195', 'API/DLL_196', 'API/DLL_197', 'API/DLL_198', 'API/DLL_199', 'API/DLL_200', 'API/DLL_201', 'API/DLL_202', 'API/DLL_203', 'API/DLL_204', 'API/DLL_205', 'API/DLL_206', 'API/DLL_207', 'API/DLL_208', 'API/DLL_209', 'API/DLL_210', 'API/DLL_211', 'API/DLL_212', 'API/DLL_213', 'API/DLL_214', 'API/DLL_215', 'API/DLL_216', 'API/DLL_217', 'API/DLL_218', 'API/DLL_219', 'API/DLL_220', 'API/DLL_221', 'API/DLL_222', 'API/DLL_223', 'API/DLL_224', 'API/DLL_225', 'API/DLL_226', 'API/DLL_227', 'API/DLL_228', 'API/DLL_229', 'API/DLL_230', 'API/DLL_231', 'API/DLL_232', 'API/DLL_233', 'API/DLL_234', 'API/DLL_235', 'API/DLL_236', 'API/DLL_237', 'API/DLL_238', 'API/DLL_239', 'API/DLL_240', 'API/DLL_241', 'API/DLL_242', 'API/DLL_243', 'API/DLL_244', 'API/DLL_245', 'API/DLL_246', 'API/DLL_247', 'API/DLL_248', 'API/DLL_249', 'API/DLL_250', 'API/DLL_251', 'API/DLL_252', 'API/DLL_253', 'API/DLL_254', 'API/DLL_255', 'API/DLL_256', 'API/DLL_257', 'API/DLL_258', 'API/DLL_259', 'API/DLL_260', 'API/DLL_261', 'API/DLL_262', 'API/DLL_263', 'API/DLL_264', 'API/DLL_265', 'API/DLL_266', 'API/DLL_267', 'API/DLL_268', 'API/DLL_269', 'API/DLL_270', 'API/DLL_271', 'API/DLL_272', 'API/DLL_273', 'API/DLL_274', 'API/DLL_275', 'API/DLL_276', 'API/DLL_277', 'API/DLL_278', 'API/DLL_279', 'API/DLL_280', 'API/DLL_281', 'API/DLL_282', 'API/DLL_283', 'API/DLL_284', 'API/DLL_285', 'API/DLL_286', 'API/DLL_287', 'API/DLL_288', 'API/DLL_289', 'API/DLL_290', 'API/DLL_291', 'API/DLL_292', 'API/DLL_293', 'API/DLL_294', 'API/DLL_295', 'API/DLL_296', 'API/DLL_297', 'API/DLL_298', 'API/DLL_299', 'API/DLL_300', 'API/DLL_301', 'API/DLL_302', 'API/DLL_303', 'API/DLL_304', 'API/DLL_305', 'API/DLL_306', 'API/DLL_307', 'API/DLL_308', 'API/DLL_309', 'API/DLL_310', 'API/DLL_311', 'API/DLL_312', 'API/DLL_313', 'API/DLL_314', 'API/DLL_315', 'API/DLL_316', 'API/DLL_317', 'API/DLL_318', 'API/DLL_319', 'API/DLL_320', 'API/DLL_321', 'API/DLL_322', 'API/DLL_323', 'API/DLL_324', 'API/DLL_325', 'API/DLL_326', 'API/DLL_327', 'API/DLL_328', 'API/DLL_329', 'API/DLL_330', 'API/DLL_331', 'API/DLL_332', 'API/DLL_333', 'API/DLL_334', 'API/DLL_335', 'API/DLL_336', 'API/DLL_337', 'API/DLL_338', 'API/DLL_339', 'API/DLL_340', 'API/DLL_341', 'API/DLL_342', 'API/DLL_343', 'API/DLL_344', 'API/DLL_345', 'API/DLL_346', 'API/DLL_347', 'API/DLL_348', 'API/DLL_349', 'API/DLL_350', 'API/DLL_351', 'API/DLL_352', 'API/DLL_353', 'API/DLL_354', 'API/DLL_355', 'API/DLL_356', 'API/DLL_357', 'API/DLL_358', 'API/DLL_359', 'API/DLL_360', 'API/DLL_361', 'API/DLL_362', 'API/DLL_363', 'API/DLL_364', 'API/DLL_365', 'API/DLL_366', 'API/DLL_367', 'API/DLL_368', 'API/DLL_369', 'API/DLL_370', 'API/DLL_371', 'API/DLL_372', 'API/DLL_373', 'API/DLL_374', 'API/DLL_375', 'API/DLL_376', 'API/DLL_377', 'API/DLL_378', 'API/DLL_379', 'API/DLL_380', 'API/DLL_381', 'API/DLL_382', 'API/DLL_383', 'API/DLL_384', 'API/DLL_385', 'API/DLL_386', 'API/DLL_387', 'API/DLL_388', 'API/DLL_389', 'API/DLL_390', 'API/DLL_391', 'API/DLL_392', 'API/DLL_393', 'API/DLL_394', 'API/DLL_395', 'API/DLL_396', 'API/DLL_397', 'API/DLL_398', 'API/DLL_399', 'API/DLL_400', 'API/DLL_401', 'API/DLL_402', 'API/DLL_403', 'API/DLL_404', 'API/DLL_405', 'API/DLL_406', 'API/DLL_407', 'API/DLL_408', 'API/DLL_409', 'API/DLL_410', 'API/DLL_411', 'API/DLL_412', 'API/DLL_413', 'API/DLL_414', 'API/DLL_415', 'API/DLL_416', 'API/DLL_417', 'API/DLL_418', 'API/DLL_419', 'API/DLL_420', 'API/DLL_421', 'API/DLL_422', 'API/DLL_423', 'API/DLL_424', 'API/DLL_425', 'API/DLL_426', 'API/DLL_427', 'API/DLL_428', 'API/DLL_429', 'API/DLL_430', 'API/DLL_431', 'API/DLL_432', 'API/DLL_433', 'API/DLL_434', 'API/DLL_435', 'API/DLL_436', 'API/DLL_437', 'API/DLL_438', 'API/DLL_439', 'API/DLL_440', 'API/DLL_441', 'API/DLL_442', 'API/DLL_443', 'API/DLL_444', 'API/DLL_445', 'API/DLL_446', 'API/DLL_447', 'API/DLL_448', 'API/DLL_449', 'API/DLL_450', 'API/DLL_451', 'API/DLL_452', 'API/DLL_453', 'API/DLL_454', 'API/DLL_455', 'API/DLL_456', 'API/DLL_457', 'API/DLL_458', 'API/DLL_459', 'API/DLL_460', 'API/DLL_461', 'API/DLL_462', 'API/DLL_463', 'API/DLL_464', 'API/DLL_465', 'API/DLL_466', 'API/DLL_467', 'API/DLL_468', 'API/DLL_469', 'API/DLL_470', 'API/DLL_471', 'API/DLL_472', 'API/DLL_473', 'API/DLL_474', 'API/DLL_475', 'API/DLL_476', 'API/DLL_477', 'API/DLL_478', 'API/DLL_479', 'API/DLL_480', 'API/DLL_481', 'API/DLL_482', 'API/DLL_483', 'API/DLL_484', 'API/DLL_485', 'API/DLL_486', 'API/DLL_487', 'API/DLL_488', 'API/DLL_489', 'API/DLL_490', 'API/DLL_491', 'API/DLL_492', 'API/DLL_493', 'API/DLL_494', 'API/DLL_495', 'API/DLL_496', 'API/DLL_497', 'API/DLL_498', 'API/DLL_499', 'API/DLL_500', 'API/DLL_501', 'API/DLL_502', 'API/DLL_503', 'API/DLL_504', 'API/DLL_505', 'API/DLL_506', 'API/DLL_507', 'API/DLL_508', 'API/DLL_509', 'API/DLL_510', 'API/DLL_511']
entropy_columns = ['Entropy0', 'Entropy1', 'Entropy2', 'Entropy3', 'Entropy4', 'Entropy5', 'Entropy6', 'Entropy7', 'Entropy8', 'Entropy9', 'Entropy10', 'Entropy11', 'Entropy12', 'Entropy13', 'Entropy14', 'Entropy15', 'Entropy16', 'Entropy17', 'Entropy18', 'Entropy19', 'Entropy20', 'Entropy21', 'Entropy22', 'Entropy23', 'Entropy24', 'Entropy25', 'Entropy26', 'Entropy27', 'Entropy28', 'Entropy29', 'Entropy30', 'Entropy31', 'Entropy32', 'Entropy33', 'Entropy34', 'Entropy35', 'Entropy36', 'Entropy37', 'Entropy38', 'Entropy39', 'Entropy40', 'Entropy41', 'Entropy42', 'Entropy43', 'Entropy44', 'Entropy45', 'Entropy46', 'Entropy47', 'Entropy48', 'Entropy49', 'Entropy50', 'Entropy51', 'Entropy52', 'Entropy53', 'Entropy54', 'Entropy55', 'Entropy56', 'Entropy57', 'Entropy58', 'Entropy59', 'Entropy60', 'Entropy61', 'Entropy62', 'Entropy63', 'Entropy64', 'Entropy65', 'Entropy66', 'Entropy67', 'Entropy68', 'Entropy69', 'Entropy70', 'Entropy71', 'Entropy72', 'Entropy73', 'Entropy74', 'Entropy75', 'Entropy76', 'Entropy77', 'Entropy78', 'Entropy79', 'Entropy80', 'Entropy81', 'Entropy82', 'Entropy83', 'Entropy84', 'Entropy85', 'Entropy86', 'Entropy87', 'Entropy88', 'Entropy89', 'Entropy90', 'Entropy91', 'Entropy92', 'Entropy93', 'Entropy94', 'Entropy95', 'Entropy96', 'Entropy97', 'Entropy98', 'Entropy99', 'Entropy100', 'Entropy101', 'Entropy102', 'Entropy103', 'Entropy104', 'Entropy105', 'Entropy106', 'Entropy107', 'Entropy108', 'Entropy109', 'Entropy110', 'Entropy111', 'Entropy112', 'Entropy113', 'Entropy114', 'Entropy115', 'Entropy116', 'Entropy117', 'Entropy118', 'Entropy119', 'Entropy120', 'Entropy121', 'Entropy122', 'Entropy123', 'Entropy124', 'Entropy125', 'Entropy126', 'Entropy127', 'Entropy128', 'Entropy129', 'Entropy130', 'Entropy131', 'Entropy132', 'Entropy133', 'Entropy134', 'Entropy135', 'Entropy136', 'Entropy137', 'Entropy138', 'Entropy139', 'Entropy140', 'Entropy141', 'Entropy142', 'Entropy143', 'Entropy144', 'Entropy145', 'Entropy146', 'Entropy147', 'Entropy148', 'Entropy149', 'Entropy150', 'Entropy151', 'Entropy152', 'Entropy153', 'Entropy154', 'Entropy155', 'Entropy156', 'Entropy157', 'Entropy158', 'Entropy159', 'Entropy160', 'Entropy161', 'Entropy162', 'Entropy163', 'Entropy164', 'Entropy165', 'Entropy166', 'Entropy167', 'Entropy168', 'Entropy169', 'Entropy170', 'Entropy171', 'Entropy172', 'Entropy173', 'Entropy174', 'Entropy175', 'Entropy176', 'Entropy177', 'Entropy178', 'Entropy179', 'Entropy180', 'Entropy181', 'Entropy182', 'Entropy183', 'Entropy184', 'Entropy185', 'Entropy186', 'Entropy187', 'Entropy188', 'Entropy189', 'Entropy190', 'Entropy191', 'Entropy192', 'Entropy193', 'Entropy194', 'Entropy195', 'Entropy196', 'Entropy197', 'Entropy198', 'Entropy199', 'Entropy200', 'Entropy201', 'Entropy202', 'Entropy203', 'Entropy204', 'Entropy205', 'Entropy206', 'Entropy207', 'Entropy208', 'Entropy209', 'Entropy210', 'Entropy211', 'Entropy212', 'Entropy213', 'Entropy214', 'Entropy215', 'Entropy216', 'Entropy217', 'Entropy218', 'Entropy219', 'Entropy220', 'Entropy221', 'Entropy222', 'Entropy223', 'Entropy224', 'Entropy225', 'Entropy226', 'Entropy227', 'Entropy228', 'Entropy229', 'Entropy230', 'Entropy231', 'Entropy232', 'Entropy233', 'Entropy234', 'Entropy235', 'Entropy236', 'Entropy237', 'Entropy238', 'Entropy239', 'Entropy240', 'Entropy241', 'Entropy242', 'Entropy243', 'Entropy244', 'Entropy245', 'Entropy246', 'Entropy247', 'Entropy248', 'Entropy249', 'Entropy250', 'Entropy251', 'Entropy252', 'Entropy253', 'Entropy254', 'Entropy255']
ep_columns = ['ENTRY_0', 'ENTRY_1', 'ENTRY_2', 'ENTRY_3', 'ENTRY_4', 'ENTRY_5', 'ENTRY_6', 'ENTRY_7', 'ENTRY_8', 'ENTRY_9', 'ENTRY_10', 'ENTRY_11', 'ENTRY_12', 'ENTRY_13', 'ENTRY_14', 'ENTRY_15', 'ENTRY_16', 'ENTRY_17', 'ENTRY_18', 'ENTRY_19', 'ENTRY_20', 'ENTRY_21', 'ENTRY_22', 'ENTRY_23', 'ENTRY_24', 'ENTRY_25', 'ENTRY_26', 'ENTRY_27', 'ENTRY_28', 'ENTRY_29', 'ENTRY_30', 'ENTRY_31', 'ENTRY_32', 'ENTRY_33', 'ENTRY_34', 'ENTRY_35', 'ENTRY_36', 'ENTRY_37', 'ENTRY_38', 'ENTRY_39', 'ENTRY_40', 'ENTRY_41', 'ENTRY_42', 'ENTRY_43', 'ENTRY_44', 'ENTRY_45', 'ENTRY_46', 'ENTRY_47', 'ENTRY_48', 'ENTRY_49']

# For Entropy
def shannon_entropy(data):
    #256 different possible values
    possible = dict(((chr(x), 0) for x in range(0, 256)))
    for byte in data:
        possible[chr(byte)] += 1
    data_len = len(data)
    entropy = 0.0
    # compute
    for i in possible:
        if possible[i] == 0:
            continue
        p = float(possible[i] / data_len)
        entropy -= p * math.log(p, 2)
    return entropy

def pre_entropy(path): # sections_entropy
    etrp_feature = [0]*16*16
    pe = pefile.PE(path)
    for section in pe.sections[:3]:
        section_idx = int(hash_md5(section.Name), 16) % 16
        etrp_idx = int((shannon_entropy(section.get_data()) * 10) // 5)
        if etrp_idx > 15:
            etrp_idx = 15
        etrp_feature[section_idx*16+etrp_idx] += 10
    return etrp_feature

# For API/DLL
def hash_md5(text):
    try:
        return md5(text).hexdigest()
    except:
        none = b"None"
        return md5(none).hexdigest()

def pre_api(path):
    pe = pefile.PE(path)
    api_dll = [0] * 512
    try:
        for iid in pe.DIRECTORY_ENTRY_IMPORT:
            for api in iid.imports:
                api_num = int(hash_md5(api.name), 16) % 125
                api_dll[api_num] += 10
    except:
        pass
    return api_dll

# For Entry_Point
def get_entry_point_address(path):
    pe = pefile.PE(path)
    return pe.get_offset_from_rva(pe.OPTIONAL_HEADER.AddressOfEntryPoint)

def pre_entrypoint(path):
    ep = get_entry_point_address(path)
    with open(path, 'rb') as f:
        data = f.read()
    ep_50 = []
    for b in data[ep:ep+50]:
        ep_50.append(b)
    if len(ep_50) != 50:
        print("ep error")
        exit()
    return ep_50

# For PE Header
def get_pe_header(path):
    pe = pefile.PE(path)
    pe_header = []
    pe_header.append(pe.DOS_HEADER.e_lfanew)
    pe_header.append(pe.FILE_HEADER.NumberOfSections)
    pe_header.append(pe.FILE_HEADER.Characteristics)
    pe_header.append(pe.OPTIONAL_HEADER.DllCharacteristics)
    pe_header.append(pe.OPTIONAL_HEADER.CheckSum)
    pe_header.append(pe.OPTIONAL_HEADER.SizeOfImage)
    pe_header.append(pe.OPTIONAL_HEADER.Subsystem)
    pe_header.append(pe.OPTIONAL_HEADER.ImageBase)
    pe_header.append(pe.OPTIONAL_HEADER.AddressOfEntryPoint)
    pe_header.append(pe.OPTIONAL_HEADER.SizeOfInitializedData)
    pe_header.append(pe.OPTIONAL_HEADER.SizeOfUninitializedData)

    # first section size
    firstS = pe.sections[0]
    sizeFirstD = firstS.SizeOfRawData
    sizeFirstV = firstS.Misc
    pe_header.append(sizeFirstD)
    pe_header.append(sizeFirstV)

    # .rsrc
    sizeRsrcD = 0
    sizeRsrcV = 0
    for section in pe.sections:
        if b'.rsrc' in section.Name:
            sizeRsrcD = section.SizeOfRawData
            sizeRsrcV = section.Misc
            break
    pe_header.append(sizeRsrcD)
    pe_header.append(sizeRsrcV)

    return pe_header
            



if __name__=="__main__":
    target_file = "C:\\Windows\\System32\\calc.exe"
    etrp_feature = pre_entropy(target_file)
    api_feature = pre_api(target_file)
    etr_feature = pre_entrypoint(target_file)

    row = api_feature + etrp_feature + etr_feature
    # row = get_pe_header(target_file)
    print(len(row))
    print(row)